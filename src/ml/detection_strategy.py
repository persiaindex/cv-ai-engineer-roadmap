from pathlib import Path
import json



def load_json_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



def count_files(directory: Path, suffix: str) -> int:
    if not directory.exists():
        return 0
    return len(list(directory.glob(f"*{suffix}")))



def validate_detection_structure(config: dict, project_root: Path) -> dict:
    train_images_dir = project_root / config["train_images_dir"]
    val_images_dir = project_root / config["val_images_dir"]
    train_labels_dir = project_root / config["train_labels_dir"]
    val_labels_dir = project_root / config["val_labels_dir"]
    dataset_yaml = project_root / config["dataset_yaml"]

    result = {
        "dataset_yaml_exists": dataset_yaml.exists(),
        "train_image_count": count_files(train_images_dir, ".jpg") + count_files(train_images_dir, ".png"),
        "val_image_count": count_files(val_images_dir, ".jpg") + count_files(val_images_dir, ".png"),
        "train_label_count": count_files(train_labels_dir, ".txt"),
        "val_label_count": count_files(val_labels_dir, ".txt"),
    }

    result["ready_for_tiny_finetune"] = (
        result["dataset_yaml_exists"]
        and result["train_image_count"] >= 1
        and result["val_image_count"] >= 1
        and result["train_label_count"] >= 1
        and result["val_label_count"] >= 1
    )

    return result



def save_strategy_report(output_path: Path, report: dict) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)