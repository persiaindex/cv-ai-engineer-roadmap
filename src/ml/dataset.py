import torch
from torch.utils.data import Dataset


class TinyInspectionDataset(Dataset):
    def __init__(self) -> None:
        self.features = torch.tensor(
            [
                [0.1, 0.2, 0.1, 0.0],
                [0.9, 0.8, 0.7, 0.9],
                [0.2, 0.1, 0.2, 0.1],
                [0.8, 0.9, 0.8, 0.7],
            ],
            dtype=torch.float32,
        )
        self.labels = torch.tensor([0, 1, 0, 1], dtype=torch.long)

    def __len__(self) -> int:
        return len(self.labels)

    def __getitem__(self, index: int):
        return self.features[index], self.labels[index]