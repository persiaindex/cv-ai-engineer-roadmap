import numpy as np

from vision.image_ops import (
    extract_basic_image_features,
    normalize_image,
    resize_nearest,
)
from vision.signal_ops import (
    extract_basic_signal_features,
    moving_average,
    normalize_signal,
)


def run_demo() -> None:
    image = np.array(
        [
            [0, 64, 128, 255],
            [10, 80, 140, 240],
            [20, 90, 150, 230],
            [30, 100, 160, 220],
        ],
        dtype=np.uint8,
    )

    signal = np.array([10, 12, 15, 14, 18, 20, 19], dtype=np.float32)

    normalized_image = normalize_image(image)
    resized_image = resize_nearest(image, new_height=2, new_width=2)
    image_features = extract_basic_image_features(image)

    normalized_signal = normalize_signal(signal)
    smoothed_signal = moving_average(signal, window_size=3)
    signal_features = extract_basic_signal_features(signal)

    print("Original image shape:", image.shape)
    print("Normalized image dtype:", normalized_image.dtype)
    print("Resized image shape:", resized_image.shape)
    print("Image features:", image_features)
    print("Normalized signal:", normalized_signal)
    print("Smoothed signal:", smoothed_signal)
    print("Signal features:", signal_features)


if __name__ == "__main__":
    run_demo()