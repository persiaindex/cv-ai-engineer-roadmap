from pathlib import Path
import json
import time

import numpy as np
import onnxruntime as ort
import torch
from torchvision import transforms
from PIL import Image

from ml.transfer_learning import build_model



def load_classification_image(image_path: Path) -> torch.Tensor:
    image = Image.open(image_path).convert("RGB")
    transform = transforms.Compose(
        [
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
        ]
    )
    tensor = transform(image).unsqueeze(0)
    return tensor



def load_trained_model(checkpoint_path: Path, num_classes: int = 2) -> torch.nn.Module:
    model = build_model(num_classes=num_classes)
    state_dict = torch.load(checkpoint_path, map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()
    return model



def export_model_to_onnx(model: torch.nn.Module, sample_input: torch.Tensor, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    torch.onnx.export(
        model,
        sample_input,
        output_path,
        input_names=["input"],
        output_names=["logits"],
        dynamic_axes={"input": {0: "batch_size"}, "logits": {0: "batch_size"}},
        opset_version=17,
    )



def run_pytorch_inference(model: torch.nn.Module, input_tensor: torch.Tensor) -> tuple[np.ndarray, float]:
    start = time.perf_counter()
    with torch.no_grad():
        output = model(input_tensor)
    elapsed = time.perf_counter() - start
    return output.numpy(), elapsed



def run_onnx_inference(onnx_path: Path, input_tensor: torch.Tensor) -> tuple[np.ndarray, float]:
    session = ort.InferenceSession(str(onnx_path), providers=["CPUExecutionProvider"])
    input_name = session.get_inputs()[0].name

    start = time.perf_counter()
    outputs = session.run(None, {input_name: input_tensor.numpy()})
    elapsed = time.perf_counter() - start
    return outputs[0], elapsed



def benchmark_and_save_report(
    image_path: Path,
    checkpoint_path: Path,
    onnx_path: Path,
    report_path: Path,
) -> dict:
    input_tensor = load_classification_image(image_path)
    model = load_trained_model(checkpoint_path)

    export_model_to_onnx(model, input_tensor, onnx_path)

    pytorch_output, pytorch_time = run_pytorch_inference(model, input_tensor)
    onnx_output, onnx_time = run_onnx_inference(onnx_path, input_tensor)

    pytorch_pred = int(np.argmax(pytorch_output, axis=1)[0])
    onnx_pred = int(np.argmax(onnx_output, axis=1)[0])

    report = {
        "image_path": str(image_path),
        "checkpoint_path": str(checkpoint_path),
        "onnx_path": str(onnx_path),
        "pytorch_time_seconds": pytorch_time,
        "onnx_time_seconds": onnx_time,
        "pytorch_predicted_class": pytorch_pred,
        "onnx_predicted_class": onnx_pred,
        "same_prediction": pytorch_pred == onnx_pred,
    }

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    return report