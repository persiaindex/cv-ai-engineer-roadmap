from __future__ import annotations

import numpy as np


Array1D = np.ndarray


def normalize_signal(signal: Array1D) -> Array1D:
    signal = signal.astype(np.float32)
    mean = np.mean(signal)
    std = np.std(signal)

    if std == 0:
        return np.zeros_like(signal)

    return (signal - mean) / std


def moving_average(signal: Array1D, window_size: int = 3) -> Array1D:
    if window_size <= 0:
        raise ValueError("window_size must be greater than 0")

    kernel = np.ones(window_size, dtype=np.float32) / window_size
    return np.convolve(signal, kernel, mode="valid")


def extract_basic_signal_features(signal: Array1D) -> dict[str, float]:
    signal = signal.astype(np.float32)
    return {
        "mean": float(np.mean(signal)),
        "std": float(np.std(signal)),
        "min": float(np.min(signal)),
        "max": float(np.max(signal)),
        "energy": float(np.sum(signal ** 2)),
    }