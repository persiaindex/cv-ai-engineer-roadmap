from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.transfer_learning import build_dataloaders, build_model, run_transfer_learning_demo



def test_build_model_output_layer_matches_num_classes() -> None:
    model = build_model(num_classes=2)
    assert model.fc.out_features == 2



def test_build_dataloaders_returns_two_classes() -> None:
    dataset_root = PROJECT_ROOT / "data" / "datasets" / "inspection_cls"
    _, _, classes = build_dataloaders(dataset_root)
    assert set(classes) == {"defect", "ok"}



def test_transfer_learning_demo_creates_checkpoint() -> None:
    dataset_root = PROJECT_ROOT / "data" / "datasets" / "inspection_cls"
    checkpoint_path = PROJECT_ROOT / "artifacts" / "test_transfer_resnet18.pt"
    result = run_transfer_learning_demo(dataset_root, checkpoint_path)
    assert checkpoint_path.exists()
    assert len(result["class_names"]) == 2
    assert result["train_loss"] >= 0
    assert result["val_loss"] >= 0