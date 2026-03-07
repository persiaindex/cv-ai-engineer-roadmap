from pathlib import Path
import sys

import numpy as np


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from vision.image_ops import extract_basic_image_features, normalize_image, resize_nearest
from vision.signal_ops import extract_basic_signal_features, moving_average, normalize_signal


def test_normalize_image_scales_to_zero_one() -> None:
    image = np.array([[0, 255]], dtype=np.uint8)
    normalized = normalize_image(image)

    assert normalized.dtype == np.float32
    assert float(normalized.min()) == 0.0
    assert float(normalized.max()) == 1.0


def test_resize_nearest_changes_shape() -> None:
    image = np.arange(16, dtype=np.uint8).reshape(4, 4)
    resized = resize_nearest(image, 2, 2)
    assert resized.shape == (2, 2)


def test_extract_basic_image_features_returns_expected_keys() -> None:
    image = np.array([[0, 10], [20, 30]], dtype=np.uint8)
    features = extract_basic_image_features(image)
    assert set(features.keys()) == {
        "mean_intensity",
        "std_intensity",
        "min_intensity",
        "max_intensity",
    }


def test_normalize_signal_returns_zero_mean_like_structure() -> None:
    signal = np.array([1, 2, 3], dtype=np.float32)
    normalized = normalize_signal(signal)
    assert normalized.shape == signal.shape
    assert np.isclose(np.mean(normalized), 0.0, atol=1e-6)


def test_moving_average_output_length() -> None:
    signal = np.array([1, 2, 3, 4, 5], dtype=np.float32)
    smoothed = moving_average(signal, window_size=3)
    assert smoothed.shape[0] == 3


def test_extract_basic_signal_features_returns_energy() -> None:
    signal = np.array([1, 2, 3], dtype=np.float32)
    features = extract_basic_signal_features(signal)
    assert "energy" in features
    assert features["energy"] == 14.0