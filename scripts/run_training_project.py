from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.evaluation import evaluate_model
from ml.transfer_learning import run_transfer_learning_demo



def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



def main() -> None:
    config_path = PROJECT_ROOT / "configs" / "training" / "transfer_baseline.json"
    config = load_config(config_path)

    dataset_root = PROJECT_ROOT / config["dataset_root"]
    checkpoint_path = PROJECT_ROOT / config["checkpoint_path"]
    evaluation_output_dir = PROJECT_ROOT / config["evaluation_output_dir"]
    project_report_path = PROJECT_ROOT / config["project_report_path"]

    train_result = run_transfer_learning_demo(dataset_root, checkpoint_path)
    eval_result = evaluate_model(dataset_root, checkpoint_path, evaluation_output_dir)

    project_report_path.parent.mkdir(parents=True, exist_ok=True)

    project_report = {
        "project_name": "inspection_training_baseline",
        "class_names": train_result["class_names"],
        "train_loss": train_result["train_loss"],
        "val_loss": train_result["val_loss"],
        "checkpoint_path": train_result["checkpoint_path"],
        "evaluation_accuracy": eval_result["accuracy"],
        "evaluation_report_path": eval_result["report_path"],
        "evaluation_csv_path": eval_result["csv_path"],
        "sample_count": eval_result["sample_count"],
    }

    with project_report_path.open("w", encoding="utf-8") as file:
        json.dump(project_report, file, indent=2)

    print(f"Project report created: {project_report_path}")
    print(f"Classes: {project_report['class_names']}")
    print(f"Train loss: {project_report['train_loss']:.6f}")
    print(f"Validation loss: {project_report['val_loss']:.6f}")
    print(f"Evaluation accuracy: {project_report['evaluation_accuracy']:.6f}")

if __name__ == "__main__":
    main()