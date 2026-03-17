from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.dataset import TinyInspectionDataset
from ml.model import TinyClassifier
from ml.train_demo import run_training_demo



def test_dataset_length() -> None:
    dataset = TinyInspectionDataset()
    assert len(dataset) == 4



def test_model_output_shape() -> None:
    model = TinyClassifier()
    dataset = TinyInspectionDataset()
    features, _ = dataset[0]
    output = model(features.unsqueeze(0))
    assert tuple(output.shape) == (1, 2)



def test_training_demo_returns_expected_shapes() -> None:
    result = run_training_demo()
    assert result["batch_shape"] == (2, 4)
    assert result["logits_shape"] == (2, 2)
    assert result["loss_before"] >= 0
    assert result["loss_after"] >= 0