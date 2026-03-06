from pathlib import Path

from core.config import load_json_config, load_yaml_config
from core.logger import setup_logger
from core.paths import get_config_path, get_project_root


def describe_environment() -> None:
    logger = setup_logger()

    project_root = get_project_root()
    json_path = get_config_path("app.json")
    yaml_path = get_config_path("app.yaml")

    json_config = load_json_config(json_path)
    yaml_config = load_yaml_config(yaml_path)

    logger.info("Project root: %s", project_root)
    logger.info("JSON config loaded: %s", json_config)
    logger.info("YAML config loaded: %s", yaml_config)


if __name__ == "__main__":
    describe_environment()