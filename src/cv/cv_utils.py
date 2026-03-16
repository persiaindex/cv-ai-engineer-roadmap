from pathlib import Path

import cv2
import numpy as np


def load_image(path: Path) -> np.ndarray:
    image = cv2.imread(str(path))
    if image is None:
        raise FileNotFoundError(f"Could not load image from: {path}")
    return image



def save_image(path: Path, image: np.ndarray) -> None:
    success = cv2.imwrite(str(path), image)
    if not success:
        raise ValueError(f"Could not save image to: {path}")



def resize_image(image: np.ndarray, width: int, height: int) -> np.ndarray:
    return cv2.resize(image, (width, height))



def convert_to_rgb(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



def draw_label(image: np.ndarray, text: str, x: int, y: int) -> np.ndarray:
    output = image.copy()
    cv2.putText(
        output,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2,
    )
    return output