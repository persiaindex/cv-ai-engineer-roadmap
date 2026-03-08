from __future__ import annotations
import numpy as np

Array2D = np.ndarray

def normalize_image(image: Array2D) -> Array2D:
    image = image.astype(np.float32)
    return image / 255.0

def resize_nearest(image: Array2D, new_height: int, new_width: int) -> Array2D:
    old_height, old_width = image.shape[:2]
    row_indices = np.linspace(0, old_height - 1, new_height).astype(int)
    col_indices = np.linspace(0, old_width - 1, new_width).astype(int)
    return image[row_indices][:, col_indices]

def extract_basic_image_features(image: Array2D) -> dict[str, float]:
    image = image.astype(np.float32)
    return {
        "mean_intensity": float(np.mean(image)),
        "std_intensity": float(np.std(image)),
        "min_intensity": float(np.min(image)),
        "max_intensity": float(np.max(image)),
    }

