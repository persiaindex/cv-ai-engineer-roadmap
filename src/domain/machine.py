from dataclasses import dataclass, field
from typing import List


@dataclass
class Machine:
    machine_id: str
    name: str
    location: str
    is_active: bool = True
    feeder_ids: List[str] = field(default_factory=list)

    def add_feeder(self, feeder_id: str) -> None:
        if feeder_id not in self.feeder_ids:
            self.feeder_ids.append(feeder_id)

    def deactivate(self) -> None:
        self.is_active = False