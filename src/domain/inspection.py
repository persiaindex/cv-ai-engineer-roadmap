from dataclasses import dataclass
from datetime import datetime


@dataclass
class Inspection:
    inspection_id: str
    machine_id: str
    defect_score: float
    image_path: str
    created_at: datetime

    def is_defective(self, threshold: float = 0.7) -> bool:
        return self.defect_score >= threshold