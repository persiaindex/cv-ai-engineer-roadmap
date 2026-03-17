from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.evaluation import evaluate_model



def main() -> None:
    dataset_root = PROJECT_ROOT / "data" / "datasets" / "inspection_cls"
    checkpoint_path = PROJECT_ROOT / "artifacts" / "transfer_resnet18.pt"
    output_dir = PROJECT_ROOT / "artifacts" / "evaluation"

    result = evaluate_model(dataset_root, checkpoint_path, output_dir)

    print(f"Sample count: {result['sample_count']}")
    print(f"Accuracy: {result['accuracy']:.6f}")
    print(f"JSON report: {result['report_path']}")
    print(f"CSV predictions: {result['csv_path']}")


if __name__ == "__main__":
    main()