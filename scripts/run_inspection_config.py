from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.pipeline import load_json_config, run_inspection_pipeline



def main() -> None:
    config_path = PROJECT_ROOT / "configs" / "inspection_config.json"
    config = load_json_config(config_path)
    result = run_inspection_pipeline(PROJECT_ROOT, config)

    print(f"Input image: {result['input_path']}")
    print(f"Contours found: {result['contour_count']}")
    print(f"Boxed output: {result['boxed_path']}")


if __name__ == "__main__":
    main()