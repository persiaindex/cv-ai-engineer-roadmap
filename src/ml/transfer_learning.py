from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, models, transforms



def build_transforms() -> transforms.Compose:
    return transforms.Compose(
        [
            transforms.Resize((128, 128)),
            transforms.ToTensor(),
        ]
    )



def build_dataloaders(dataset_root: Path) -> tuple[DataLoader, DataLoader, list[str]]:
    transform = build_transforms()

    train_dataset = datasets.ImageFolder(dataset_root / "train", transform=transform)
    val_dataset = datasets.ImageFolder(dataset_root / "val", transform=transform)

    train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=2, shuffle=False)

    return train_loader, val_loader, train_dataset.classes



def build_model(num_classes: int) -> nn.Module:
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)

    for parameter in model.parameters():
        parameter.requires_grad = False

    in_features = model.fc.in_features
    model.fc = nn.Linear(in_features, num_classes)

    return model



def train_one_epoch(model: nn.Module, dataloader: DataLoader, criterion: nn.Module, optimizer: torch.optim.Optimizer) -> float:
    model.train()
    total_loss = 0.0
    batch_count = 0

    for inputs, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += float(loss.item())
        batch_count += 1

    return total_loss / batch_count



def validate_one_epoch(model: nn.Module, dataloader: DataLoader, criterion: nn.Module) -> float:
    model.eval()
    total_loss = 0.0
    batch_count = 0

    with torch.no_grad():
        for inputs, labels in dataloader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            total_loss += float(loss.item())
            batch_count += 1

    return total_loss / batch_count



def run_transfer_learning_demo(dataset_root: Path, checkpoint_path: Path) -> dict:
    train_loader, val_loader, classes = build_dataloaders(dataset_root)
    model = build_model(num_classes=len(classes))
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.fc.parameters(), lr=0.01)

    train_loss = train_one_epoch(model, train_loader, criterion, optimizer)
    val_loss = validate_one_epoch(model, val_loader, criterion)

    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), checkpoint_path)

    return {
        "class_names": classes,
        "train_loss": train_loss,
        "val_loss": val_loss,
        "checkpoint_path": str(checkpoint_path),
    }