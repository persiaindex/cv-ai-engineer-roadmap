from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.detection_utils import compute_precision_recall, intersection_over_union, non_max_suppression



def test_intersection_over_union_returns_expected_range() -> None:
    box_a = (0.0, 0.0, 10.0, 10.0)
    box_b = (5.0, 5.0, 15.0, 15.0)
    iou = intersection_over_union(box_a, box_b)
    assert 0.0 < iou < 1.0



def test_non_max_suppression_reduces_overlapping_boxes() -> None:
    boxes = [
        {"label": "defect", "score": 0.95, "box": (10.0, 10.0, 50.0, 50.0)},
        {"label": "defect", "score": 0.80, "box": (12.0, 12.0, 48.0, 48.0)},
        {"label": "defect", "score": 0.60, "box": (100.0, 100.0, 140.0, 140.0)},
    ]
    kept = non_max_suppression(boxes, iou_threshold=0.5)
    assert len(kept) == 2



def test_compute_precision_recall_returns_valid_values() -> None:
    metrics = compute_precision_recall(tp=2, fp=1, fn=1)
    assert metrics["precision"] == 2 / 3
    assert metrics["recall"] == 2 / 3