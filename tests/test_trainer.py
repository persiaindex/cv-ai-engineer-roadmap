from pathlib import Path
import sys

import torch
from torch import nn
from torch.utils.data import DataLoader, random_split

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.dataset import TinyInspectionDataset
from ml.model import TinyClassifier
from ml.trainer import calculate_accuracy, run_epoch, train_model



def test_calculate_accuracy_returns_valid_value() -> None:
    logits = torch.tensor([[0.1, 0.9], [0.8, 0.2]], dtype=torch.float32)
    labels = torch.tensor([1, 0], dtype=torch.long)
    accuracy = calculate_accuracy(logits, labels)
    assert accuracy == 1.0



def test_run_epoch_returns_loss_and_accuracy() -> None:
    dataset = TinyInspectionDataset()
    loader = DataLoader(dataset, batch_size=2, shuffle=False)
    model = TinyClassifier()
    criterion = nn.CrossEntropyLoss()
    metrics = run_epoch(model, loader, criterion)
    assert "loss" in metrics
    assert "accuracy" in metrics
    assert metrics["loss"] >= 0



def test_train_model_saves_checkpoint() -> None:
    dataset = TinyInspectionDataset()
    train_dataset, val_dataset = random_split(
        dataset,
        lengths=[3, 1],
        generator=torch.Generator().manual_seed(42),
    )

    train_loader = DataLoader(train_dataset, batch_size=2, shuffle=False)
    val_loader = DataLoader(val_dataset, batch_size=1, shuffle=False)

    model = TinyClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    checkpoint_path = PROJECT_ROOT / "artifacts" / "test_tiny_classifier.pt"

    history = train_model(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        epochs=3,
        criterion=criterion,
        optimizer=optimizer,
        checkpoint_path=checkpoint_path,
    )

    assert checkpoint_path.exists()
    assert len(history["train_loss"]) == 3
    assert len(history["val_loss"]) == 3