from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.detection_utils import (
    compute_precision_recall,
    intersection_over_union,
    non_max_suppression,
    save_detection_report,
)



def main() -> None:
    ground_truth_box = (20.0, 20.0, 80.0, 80.0)
    predicted_box = (25.0, 25.0, 78.0, 78.0)
    iou = intersection_over_union(ground_truth_box, predicted_box)

    boxes = [
        {"label": "defect", "score": 0.95, "box": (20.0, 20.0, 80.0, 80.0)},
        {"label": "defect", "score": 0.80, "box": (22.0, 22.0, 79.0, 79.0)},
        {"label": "defect", "score": 0.60, "box": (120.0, 120.0, 170.0, 170.0)},
    ]

    kept_boxes = non_max_suppression(boxes, iou_threshold=0.5)
    metrics = compute_precision_recall(tp=1, fp=1, fn=1)

    report = {
        "iou_example": iou,
        "boxes_before_nms": len(boxes),
        "boxes_after_nms": len(kept_boxes),
        "precision": metrics["precision"],
        "recall": metrics["recall"],
    }

    output_path = PROJECT_ROOT / "artifacts" / "detection" / "detection_metrics_report.json"
    save_detection_report(output_path, report)

    print(f"IoU example: {iou:.6f}")
    print(f"Boxes before NMS: {len(boxes)}")
    print(f"Boxes after NMS: {len(kept_boxes)}")
    print(f"Precision: {metrics['precision']:.6f}")
    print(f"Recall: {metrics['recall']:.6f}")
    print(f"Report saved to: {output_path}")


if __name__ == "__main__":
    main()