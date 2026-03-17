from pathlib import Path
import csv
import json

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from ml.transfer_learning import build_model



def build_eval_dataloader(dataset_root: Path) -> tuple[DataLoader, list[str], list[tuple[str, int]]]:
    transform = transforms.Compose(
        [
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
        ]
    )

    dataset = datasets.ImageFolder(dataset_root / "val", transform=transform)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False)
    return dataloader, dataset.classes, dataset.samples



def compute_confusion_matrix(num_classes: int, y_true: list[int], y_pred: list[int]) -> list[list[int]]:
    matrix = [[0 for _ in range(num_classes)] for _ in range(num_classes)]

    for true_label, predicted_label in zip(y_true, y_pred):
        matrix[true_label][predicted_label] += 1

    return matrix



def evaluate_model(dataset_root: Path, checkpoint_path: Path, output_dir: Path) -> dict:
    dataloader, class_names, samples = build_eval_dataloader(dataset_root)
    model = build_model(num_classes=len(class_names))
    model.load_state_dict(torch.load(checkpoint_path, map_location="cpu"))
    model.eval()

    y_true: list[int] = []
    y_pred: list[int] = []
    records: list[dict[str, str | int | bool]] = []

    with torch.no_grad():
        for index, (inputs, labels) in enumerate(dataloader):
            outputs = model(inputs)
            predictions = torch.argmax(outputs, dim=1)

            true_idx = int(labels.item())
            pred_idx = int(predictions.item())

            y_true.append(true_idx)
            y_pred.append(pred_idx)

            image_path = samples[index][0]
            records.append(
                {
                    "image_path": image_path,
                    "true_label": class_names[true_idx],
                    "predicted_label": class_names[pred_idx],
                    "correct": true_idx == pred_idx,
                }
            )

    confusion_matrix = compute_confusion_matrix(len(class_names), y_true, y_pred)
    correct_count = sum(1 for true_idx, pred_idx in zip(y_true, y_pred) if true_idx == pred_idx)
    accuracy = correct_count / len(y_true) if y_true else 0.0

    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "evaluation_report.json"
    csv_path = output_dir / "evaluation_predictions.csv"

    report = {
        "class_names": class_names,
        "sample_count": len(y_true),
        "accuracy": accuracy,
        "confusion_matrix": confusion_matrix,
        "records": records,
    }

    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    with csv_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["image_path", "true_label", "predicted_label", "correct"])
        writer.writeheader()
        writer.writerows(records)

    return {
        "accuracy": accuracy,
        "sample_count": len(y_true),
        "report_path": str(report_path),
        "csv_path": str(csv_path),
    }