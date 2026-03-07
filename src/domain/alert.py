from dataclasses import dataclass


@dataclass
class Alert:
    alert_id: str
    source_type: str
    source_id: str
    message: str
    severity: str
    is_open: bool = True

    def close(self) -> None:
        self.is_open = False