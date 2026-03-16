from pathlib import Path
import sys

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.cv_utils import convert_to_rgb, draw_label, resize_image



def test_resize_image_returns_expected_shape() -> None:
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    resized = resize_image(image, width=50, height=40)
    assert resized.shape == (40, 50, 3)



def test_convert_to_rgb_keeps_shape() -> None:
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    converted = convert_to_rgb(image)
    assert converted.shape == image.shape



def test_draw_label_returns_image_with_same_shape() -> None:
    image = np.zeros((60, 80, 3), dtype=np.uint8)
    output = draw_label(image, "Test", x=5, y=20)
    assert output.shape == image.shape