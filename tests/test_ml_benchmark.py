from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = PROJECT_ROOT / "apps"

if str(APPS_PATH) not in sys.path:
    sys.path.insert(0, str(APPS_PATH))

from ml_service.benchmark import benchmark_preprocessing, build_benchmark_report, load_benchmark_model, benchmark_inference



def test_benchmark_preprocessing_returns_positive_value() -> None:
    value = benchmark_preprocessing(iterations=10)
    assert value > 0



def test_benchmark_inference_returns_expected_keys() -> None:
    model = load_benchmark_model()
    result = benchmark_inference(model, batch_size=2, iterations=10)
    assert result["batch_size"] == 2
    assert result["average_seconds"] > 0
    assert result["throughput_samples_per_second"] > 0



def test_build_benchmark_report_contains_batch_entries() -> None:
    report = build_benchmark_report()
    assert report["device"] == "cpu"
    assert "batch_1" in report
    assert "batch_4" in report