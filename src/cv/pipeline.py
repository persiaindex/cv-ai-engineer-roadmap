from pathlib import Path
import json

import cv2

from cv.inspection import (
    clean_mask,
    create_inspection_sample,
    draw_defect_boxes,
    find_defect_contours,
    to_grayscale,
)



def load_json_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



def threshold_defects_with_value(gray, threshold_value: int):
    _, mask = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY_INV)
    return mask



def run_inspection_pipeline(project_root: Path, config: dict) -> dict:
    input_path = project_root / config["input_image"]
    gray_path = project_root / config["output_gray"]
    mask_path = project_root / config["output_mask"]
    cleaned_path = project_root / config["output_cleaned"]
    boxed_path = project_root / config["output_boxed"]

    input_path.parent.mkdir(parents=True, exist_ok=True)
    boxed_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        create_inspection_sample(input_path)

    image = cv2.imread(str(input_path))
    if image is None:
        raise FileNotFoundError(f"Could not load input image: {input_path}")

    gray = to_grayscale(image)
    mask = threshold_defects_with_value(gray, config["threshold_value"])
    cleaned = clean_mask(mask)
    contours = find_defect_contours(cleaned)
    boxed = draw_defect_boxes(image, contours, min_area=config["min_area"])

    cv2.imwrite(str(gray_path), gray)
    cv2.imwrite(str(mask_path), mask)
    cv2.imwrite(str(cleaned_path), cleaned)
    cv2.imwrite(str(boxed_path), boxed)

    return {
        "input_path": str(input_path),
        "boxed_path": str(boxed_path),
        "contour_count": len(contours),
    }