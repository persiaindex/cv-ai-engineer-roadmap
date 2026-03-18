from pathlib import Path
import sys

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.model import TinyClassifier


CLASS_NAMES = ["ok", "defect"]
INPUT_DIM = 4



def load_demo_model() -> TinyClassifier:
    model = TinyClassifier(input_dim=INPUT_DIM, hidden_dim=8, num_classes=len(CLASS_NAMES))

    checkpoint_path = PROJECT_ROOT / "artifacts" / "tiny_classifier.pt"
    if checkpoint_path.exists():
        state_dict = torch.load(checkpoint_path, map_location="cpu")
        model.load_state_dict(state_dict)

    model.eval()
    return model


MODEL = load_demo_model()



def predict_from_features(features: list[float]) -> dict:
    if len(features) != INPUT_DIM:
        raise ValueError(f"Expected {INPUT_DIM} features, got {len(features)}")

    input_tensor = torch.tensor([features], dtype=torch.float32)

    with torch.no_grad():
        logits = MODEL(input_tensor)
        probabilities = torch.softmax(logits, dim=1)[0]
        predicted_class = int(torch.argmax(probabilities).item())

    return {
        "predicted_class": predicted_class,
        "predicted_label": CLASS_NAMES[predicted_class],
        "probabilities": [float(value) for value in probabilities.tolist()],
    }



def get_metadata() -> dict:
    return {
        "model_name": "tiny_classifier",
        "model_type": "pytorch_mlp",
        "class_names": CLASS_NAMES,
        "input_dim": INPUT_DIM,
    }