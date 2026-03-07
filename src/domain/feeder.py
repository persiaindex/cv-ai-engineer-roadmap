from dataclasses import dataclass


@dataclass
class Feeder:
    feeder_id: str
    machine_id: str
    material_type: str
    fill_level: float

    def needs_refill(self, threshold: float = 20.0) -> bool:
        return self.fill_level < threshold