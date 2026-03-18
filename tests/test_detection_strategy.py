from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.detection_strategy import load_json_config, validate_detection_structure



def test_load_json_config_reads_target_model() -> None:
    config_path = PROJECT_ROOT / "configs" / "detection" / "fine_tune_tiny.json"
    config = load_json_config(config_path)
    assert "target_model" in config



def test_validate_detection_structure_returns_expected_keys() -> None:
    config_path = PROJECT_ROOT / "configs" / "detection" / "fine_tune_tiny.json"
    config = load_json_config(config_path)
    result = validate_detection_structure(config, PROJECT_ROOT)
    assert "dataset_yaml_exists" in result
    assert "ready_for_tiny_finetune" in result