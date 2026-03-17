from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader



def calculate_accuracy(logits: torch.Tensor, labels: torch.Tensor) -> float:
    predictions = torch.argmax(logits, dim=1)
    correct = (predictions == labels).sum().item()
    return correct / len(labels)



def run_epoch(
    model: nn.Module,
    dataloader: DataLoader,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer | None = None,
) -> dict[str, float]:
    is_training = optimizer is not None
    model.train() if is_training else model.eval()

    total_loss = 0.0
    total_accuracy = 0.0
    batch_count = 0

    for features, labels in dataloader:
        if is_training:
            optimizer.zero_grad()

        with torch.set_grad_enabled(is_training):
            logits = model(features)
            loss = criterion(logits, labels)

            if is_training:
                loss.backward()
                optimizer.step()

        total_loss += float(loss.item())
        total_accuracy += calculate_accuracy(logits, labels)
        batch_count += 1

    return {
        "loss": total_loss / batch_count,
        "accuracy": total_accuracy / batch_count,
    }



def train_model(
    model: nn.Module,
    train_loader: DataLoader,
    val_loader: DataLoader,
    epochs: int,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    checkpoint_path: Path,
) -> dict[str, list[float] | float]:
    history = {
        "train_loss": [],
        "train_accuracy": [],
        "val_loss": [],
        "val_accuracy": [],
    }

    best_val_loss = float("inf")

    for _ in range(epochs):
        train_metrics = run_epoch(model, train_loader, criterion, optimizer)
        val_metrics = run_epoch(model, val_loader, criterion)

        history["train_loss"].append(train_metrics["loss"])
        history["train_accuracy"].append(train_metrics["accuracy"])
        history["val_loss"].append(val_metrics["loss"])
        history["val_accuracy"].append(val_metrics["accuracy"])

        if val_metrics["loss"] < best_val_loss:
            best_val_loss = val_metrics["loss"]
            checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
            torch.save(model.state_dict(), checkpoint_path)

    history["best_val_loss"] = best_val_loss
    return history