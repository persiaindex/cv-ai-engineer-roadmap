from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.onnx_export import benchmark_and_save_report



def main() -> None:
    image_path = PROJECT_ROOT / "data" / "datasets" / "inspection_cls" / "val" / "defect"
    image_files = list(image_path.glob("*.jpg")) + list(image_path.glob("*.png"))
    if not image_files:
        raise FileNotFoundError("No validation image found in data/datasets/inspection_cls/val/defect")

    sample_image = image_files[0]
    checkpoint_path = PROJECT_ROOT / "artifacts" / "transfer_resnet18.pt"
    onnx_path = PROJECT_ROOT / "artifacts" / "onnx" / "transfer_resnet18.onnx"
    report_path = PROJECT_ROOT / "artifacts" / "onnx" / "onnx_benchmark_report.json"

    report = benchmark_and_save_report(sample_image, checkpoint_path, onnx_path, report_path)

    print(f"Sample image: {sample_image}")
    print(f"ONNX file: {onnx_path}")
    print(f"PyTorch time: {report['pytorch_time_seconds']:.6f}")
    print(f"ONNX time: {report['onnx_time_seconds']:.6f}")
    print(f"Same prediction: {report['same_prediction']}")
    print(f"Benchmark report: {report_path}")


if __name__ == "__main__":
    main()