from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.transfer_learning import run_transfer_learning_demo



def main() -> None:
    dataset_root = PROJECT_ROOT / "data" / "datasets" / "inspection_cls"
    checkpoint_path = PROJECT_ROOT / "artifacts" / "transfer_resnet18.pt"

    result = run_transfer_learning_demo(dataset_root, checkpoint_path)

    print(f"Classes: {result['class_names']}")
    print(f"Train loss: {result['train_loss']:.6f}")
    print(f"Validation loss: {result['val_loss']:.6f}")
    print(f"Checkpoint saved to: {result['checkpoint_path']}")


if __name__ == "__main__":
    main()