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
from ml.trainer import train_model



def main() -> None:
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
    checkpoint_path = PROJECT_ROOT / "artifacts" / "tiny_classifier.pt"

    history = train_model(
        model=model,
        train_loader=train_loader,
        val_loader=val_loader,
        epochs=5,
        criterion=criterion,
        optimizer=optimizer,
        checkpoint_path=checkpoint_path,
    )

    print(f"Train loss history: {history['train_loss']}")
    print(f"Validation loss history: {history['val_loss']}")
    print(f"Best validation loss: {history['best_val_loss']:.6f}")
    print(f"Checkpoint saved to: {checkpoint_path}")


if __name__ == "__main__":
    main()