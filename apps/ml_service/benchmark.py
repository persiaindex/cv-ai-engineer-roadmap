from pathlib import Path
import statistics
import sys
import time

import torch

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.model import TinyClassifier


INPUT_DIM = 4
CLASS_NAMES = ["ok", "defect"]



def load_benchmark_model() -> TinyClassifier:
    model = TinyClassifier(input_dim=INPUT_DIM, hidden_dim=8, num_classes=len(CLASS_NAMES))

    checkpoint_path = PROJECT_ROOT / "artifacts" / "tiny_classifier.pt"
    if checkpoint_path.exists():
        state_dict = torch.load(checkpoint_path, map_location="cpu")
        model.load_state_dict(state_dict)

    model.eval()
    return model



def benchmark_preprocessing(iterations: int = 1000) -> float:
    times = []

    for _ in range(iterations):
        start = time.perf_counter()
        _ = torch.tensor([[0.1, 0.2, 0.1, 0.0]], dtype=torch.float32)
        times.append(time.perf_counter() - start)

    return statistics.mean(times)



def benchmark_inference(model: TinyClassifier, batch_size: int, iterations: int = 200) -> dict[str, float]:
    input_tensor = torch.tensor([[0.1, 0.2, 0.1, 0.0]] * batch_size, dtype=torch.float32)
    times = []

    with torch.no_grad():
        for _ in range(iterations):
            start = time.perf_counter()
            _ = model(input_tensor)
            times.append(time.perf_counter() - start)

    avg_time = statistics.mean(times)
    throughput = batch_size / avg_time if avg_time > 0 else 0.0

    return {
        "batch_size": batch_size,
        "average_seconds": avg_time,
        "throughput_samples_per_second": throughput,
    }



def build_benchmark_report() -> dict:
    model = load_benchmark_model()
    preprocessing_time = benchmark_preprocessing()
    batch1 = benchmark_inference(model, batch_size=1)
    batch4 = benchmark_inference(model, batch_size=4)

    return {
        "model_name": "tiny_classifier",
        "device": "cpu",
        "preprocessing_average_seconds": preprocessing_time,
        "batch_1": batch1,
        "batch_4": batch4,
    }