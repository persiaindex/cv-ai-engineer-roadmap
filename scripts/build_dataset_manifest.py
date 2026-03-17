from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.dataset_utils import build_manifest


def main() -> None:
    dataset_dir = PROJECT_ROOT / "data" / "datasets" / "inspection_v1"
    output_path = dataset_dir / "manifest.json"

    manifest = build_manifest(dataset_dir)

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(manifest, file, indent=2)

    print(f"Manifest created: {output_path}")
    print(f"Number of records: {len(manifest)}")


if __name__ == "__main__":
    main()