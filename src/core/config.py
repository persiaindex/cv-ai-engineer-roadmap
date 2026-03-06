from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


ConfigDict = dict[str, Any]


def load_json_config(path: Path) -> ConfigDict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml_config(path: Path) -> ConfigDict:
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)
    
def load_config(path: Path) -> dict[str, Any]:
    if path.suffix == ".json":
        return load_json_config(path)
    if path.suffix in {".yaml", ".yml"}:
        return load_yaml_config(path)
    raise ValueError(f"Unsupported config format: {path.suffix}")    