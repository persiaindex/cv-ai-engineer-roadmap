from pathlib import Path
import sys

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.inspection import clean_mask, draw_defect_boxes, find_defect_contours, threshold_defects, to_grayscale



def test_to_grayscale_reduces_channel_dimension() -> None:
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    gray = to_grayscale(image)
    assert gray.shape == (100, 100)



def test_threshold_defects_returns_2d_mask() -> None:
    gray = np.full((50, 50), 200, dtype=np.uint8)
    gray[20:30, 20:30] = 10
    mask = threshold_defects(gray)
    assert mask.shape == gray.shape
    assert mask.dtype == np.uint8



def test_find_defect_contours_detects_object() -> None:
    mask = np.zeros((80, 80), dtype=np.uint8)
    mask[20:40, 20:40] = 255
    cleaned = clean_mask(mask)
    contours = find_defect_contours(cleaned)
    assert len(contours) >= 1



def test_draw_defect_boxes_preserves_shape() -> None:
    image = np.zeros((80, 80, 3), dtype=np.uint8)
    mask = np.zeros((80, 80), dtype=np.uint8)
    mask[20:40, 20:40] = 255
    contours = find_defect_contours(mask)
    output = draw_defect_boxes(image, contours, min_area=10)
    assert output.shape == image.shape