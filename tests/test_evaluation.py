from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.evaluation import compute_confusion_matrix, evaluate_model



def test_compute_confusion_matrix_shape() -> None:
    matrix = compute_confusion_matrix(2, [0, 1, 0], [0, 1, 1])
    assert len(matrix) == 2
    assert len(matrix[0]) == 2
    assert matrix[0][0] == 1



def test_evaluate_model_creates_outputs() -> None:
    dataset_root = PROJECT_ROOT / "data" / "datasets" / "inspection_cls"
    checkpoint_path = PROJECT_ROOT / "artifacts" / "transfer_resnet18.pt"
    output_dir = PROJECT_ROOT / "artifacts" / "evaluation_test"

    result = evaluate_model(dataset_root, checkpoint_path, output_dir)

    assert result["sample_count"] >= 1
    assert Path(result["report_path"]).exists()
    assert Path(result["csv_path"]).exists()
    assert result["accuracy"] >= 0