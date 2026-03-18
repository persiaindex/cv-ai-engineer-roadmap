from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.detection_strategy import load_json_config, save_strategy_report, validate_detection_structure



def main() -> None:
    config_path = PROJECT_ROOT / "configs" / "detection" / "fine_tune_tiny.json"
    report_path = PROJECT_ROOT / "artifacts" / "detection" / "fine_tune_strategy_report.json"

    config = load_json_config(config_path)
    structure_report = validate_detection_structure(config, PROJECT_ROOT)

    report = {
        "target_model": config["target_model"],
        "image_size": config["image_size"],
        "epochs": config["epochs"],
        "batch_size": config["batch_size"],
        "device_strategy": config["device_strategy"],
        "notes": config["notes"],
        "structure_report": structure_report,
    }

    save_strategy_report(report_path, report)

    print(f"Strategy report created: {report_path}")
    print(f"Train images: {structure_report['train_image_count']}")
    print(f"Validation images: {structure_report['val_image_count']}")
    print(f"Ready for tiny fine-tune: {structure_report['ready_for_tiny_finetune']}")


if __name__ == "__main__":
    main()