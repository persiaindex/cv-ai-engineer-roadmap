from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
APPS_PATH = PROJECT_ROOT / "apps"

if str(APPS_PATH) not in sys.path:
    sys.path.insert(0, str(APPS_PATH))

from ml_service.benchmark import build_benchmark_report



def main() -> None:
    report = build_benchmark_report()
    output_path = PROJECT_ROOT / "artifacts" / "ml_service" / "ml_benchmark_report.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print(f"Preprocessing avg seconds: {report['preprocessing_average_seconds']:.8f}")
    print(f"Batch 1 avg seconds: {report['batch_1']['average_seconds']:.8f}")
    print(f"Batch 1 throughput: {report['batch_1']['throughput_samples_per_second']:.2f}")
    print(f"Batch 4 avg seconds: {report['batch_4']['average_seconds']:.8f}")
    print(f"Batch 4 throughput: {report['batch_4']['throughput_samples_per_second']:.2f}")
    print(f"Benchmark report: {output_path}")


if __name__ == "__main__":
    main()