from pathlib import Path
import json
import sys

import cv2

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.dataset_utils import build_manifest
from cv.inspection import clean_mask, draw_defect_boxes, find_defect_contours, threshold_defects, to_grayscale



def main() -> None:
    dataset_dir = PROJECT_ROOT / "data" / "datasets" / "inspection_v1"
    output_dir = PROJECT_ROOT / "projects" / "pcb_defect_baseline" / "output"
    report_path = output_dir / "baseline_report.json"

    output_dir.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest(dataset_dir)

    processed_records = []
    total_contours = 0

    for record in manifest:
        image_path = Path(record["image_path"])
        image = cv2.imread(str(image_path))
        if image is None:
            raise FileNotFoundError(f"Could not load image: {image_path}")

        gray = to_grayscale(image)
        mask = threshold_defects(gray)
        cleaned = clean_mask(mask)
        contours = find_defect_contours(cleaned)
        boxed = draw_defect_boxes(image, contours, min_area=20)

        output_image_path = output_dir / f"boxed_{record['image_name']}"
        cv2.imwrite(str(output_image_path), boxed)

        contour_count = len(contours)
        total_contours += contour_count

        processed_records.append(
            {
                "image_name": record["image_name"],
                "label": record["label"],
                "split": record["split"],
                "contour_count": contour_count,
                "output_image": str(output_image_path),
            }
        )

    report = {
        "dataset_name": "inspection_v1",
        "image_count": len(processed_records),
        "total_contours": total_contours,
        "records": processed_records,
    }

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print(f"Report created: {report_path}")
    print(f"Images processed: {report['image_count']}")
    print(f"Total contours: {report['total_contours']}")


if __name__ == "__main__":
    main()