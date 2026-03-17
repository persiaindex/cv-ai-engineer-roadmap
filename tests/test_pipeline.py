from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from cv.pipeline import load_json_config, run_inspection_pipeline



def test_load_json_config_reads_threshold() -> None:
    config_path = PROJECT_ROOT / "configs" / "inspection_config.json"
    config = load_json_config(config_path)
    assert config["threshold_value"] == 80



def test_run_inspection_pipeline_returns_result() -> None:
    config_path = PROJECT_ROOT / "configs" / "inspection_config.json"
    config = load_json_config(config_path)
    result = run_inspection_pipeline(PROJECT_ROOT, config)
    assert result["contour_count"] >= 1
    assert Path(result["boxed_path"]).exists()