from pathlib import Path
import json


Box = tuple[float, float, float, float]



def intersection_over_union(box_a: Box, box_b: Box) -> float:
    ax1, ay1, ax2, ay2 = box_a
    bx1, by1, bx2, by2 = box_b

    inter_x1 = max(ax1, bx1)
    inter_y1 = max(ay1, by1)
    inter_x2 = min(ax2, bx2)
    inter_y2 = min(ay2, by2)

    inter_width = max(0.0, inter_x2 - inter_x1)
    inter_height = max(0.0, inter_y2 - inter_y1)
    inter_area = inter_width * inter_height

    area_a = max(0.0, ax2 - ax1) * max(0.0, ay2 - ay1)
    area_b = max(0.0, bx2 - bx1) * max(0.0, by2 - by1)

    union_area = area_a + area_b - inter_area
    if union_area == 0:
        return 0.0

    return inter_area / union_area



def non_max_suppression(boxes: list[dict], iou_threshold: float) -> list[dict]:
    sorted_boxes = sorted(boxes, key=lambda item: item["score"], reverse=True)
    selected: list[dict] = []

    while sorted_boxes:
        current = sorted_boxes.pop(0)
        selected.append(current)

        remaining = []
        for candidate in sorted_boxes:
            iou = intersection_over_union(current["box"], candidate["box"])
            if iou < iou_threshold:
                remaining.append(candidate)

        sorted_boxes = remaining

    return selected



def compute_precision_recall(tp: int, fp: int, fn: int) -> dict[str, float]:
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    return {
        "precision": precision,
        "recall": recall,
    }



def save_detection_report(output_path: Path, report: dict) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)