from pathlib import Path
import sys

import cv2

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.inspection import (
    clean_mask,
    create_inspection_sample,
    draw_defect_boxes,
    find_defect_contours,
    threshold_defects,
    to_grayscale,
)



def main() -> None:
    input_path = PROJECT_ROOT / "data" / "images" / "inspection_input.png"
    gray_path = PROJECT_ROOT / "data" / "output" / "inspection_gray.png"
    mask_path = PROJECT_ROOT / "data" / "output" / "inspection_mask.png"
    cleaned_path = PROJECT_ROOT / "data" / "output" / "inspection_cleaned.png"
    boxed_path = PROJECT_ROOT / "data" / "output" / "inspection_boxed.png"

    input_path.parent.mkdir(parents=True, exist_ok=True)
    boxed_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        create_inspection_sample(input_path)

    image = cv2.imread(str(input_path))
    gray = to_grayscale(image)
    mask = threshold_defects(gray)
    cleaned = clean_mask(mask)
    contours = find_defect_contours(cleaned)
    boxed = draw_defect_boxes(image, contours)

    cv2.imwrite(str(gray_path), gray)
    cv2.imwrite(str(mask_path), mask)
    cv2.imwrite(str(cleaned_path), cleaned)
    cv2.imwrite(str(boxed_path), boxed)

    print(f"Input image: {input_path}")
    print(f"Contours found: {len(contours)}")
    print(f"Boxed output: {boxed_path}")


if __name__ == "__main__":
    main()