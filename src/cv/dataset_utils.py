from pathlib import Path
import csv


ALLOWED_LABELS = {"ok", "defect"}
ALLOWED_SPLITS = {"train", "val", "test"}


def load_labels_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def validate_labels(rows: list[dict[str, str]]) -> None:
    required_columns = {"image_name", "label", "split", "notes"}

    for row in rows:
        if set(row.keys()) != required_columns:
            raise ValueError("CSV columns do not match the expected format.")

        if row["label"] not in ALLOWED_LABELS:
            raise ValueError(f"Invalid label: {row['label']}")

        if row["split"] not in ALLOWED_SPLITS:
            raise ValueError(f"Invalid split: {row['split']}")


def build_manifest(dataset_dir: Path) -> list[dict[str, str]]:
    labels_path = dataset_dir / "labels.csv"
    images_dir = dataset_dir / "images"

    rows = load_labels_csv(labels_path)
    validate_labels(rows)

    manifest: list[dict[str, str]] = []

    for row in rows:
        image_path = images_dir / row["image_name"]
        if not image_path.exists():
            raise FileNotFoundError(f"Missing image file: {image_path}")

        manifest.append(
            {
                "image_name": row["image_name"],
                "label": row["label"],
                "split": row["split"],
                "image_path": str(image_path),
            }
        )

    return manifest