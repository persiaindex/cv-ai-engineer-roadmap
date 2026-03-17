from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.dataset_utils import build_manifest, load_labels_csv, validate_labels


def test_load_labels_csv_returns_rows() -> None:
    labels_path = PROJECT_ROOT / "data" / "datasets" / "inspection_v1" / "labels.csv"
    rows = load_labels_csv(labels_path)
    assert len(rows) >= 1


def test_validate_labels_accepts_valid_rows() -> None:
    rows = [
        {
            "image_name": "img_001.png",
            "label": "ok",
            "split": "train",
            "notes": "sample",
        }
    ]
    validate_labels(rows)


def test_build_manifest_returns_records() -> None:
    dataset_dir = PROJECT_ROOT / "data" / "datasets" / "inspection_v1"
    manifest = build_manifest(dataset_dir)
    assert len(manifest) >= 1
    assert "image_path" in manifest[0]