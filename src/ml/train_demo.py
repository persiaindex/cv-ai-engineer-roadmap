import torch
from torch import nn
from torch.utils.data import DataLoader

from ml.dataset import TinyInspectionDataset
from ml.model import TinyClassifier



def run_training_demo() -> dict:
    dataset = TinyInspectionDataset()
    loader = DataLoader(dataset, batch_size=2, shuffle=False)

    model = TinyClassifier()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    batch_features, batch_labels = next(iter(loader))
    logits_before = model(batch_features)
    loss_before = criterion(logits_before, batch_labels)

    optimizer.zero_grad()
    loss_before.backward()
    optimizer.step()

    logits_after = model(batch_features)
    loss_after = criterion(logits_after, batch_labels)

    return {
        "batch_shape": tuple(batch_features.shape),
        "logits_shape": tuple(logits_before.shape),
        "loss_before": float(loss_before.item()),
        "loss_after": float(loss_after.item()),
    }