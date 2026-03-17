import torch
from torch import nn


class TinyClassifier(nn.Module):
    def __init__(self, input_dim: int = 4, hidden_dim: int = 8, num_classes: int = 2) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.network(x)