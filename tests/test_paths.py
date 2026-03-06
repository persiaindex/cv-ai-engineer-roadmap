from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from core.paths import get_project_root


def test_get_project_root() -> None:
    root = get_project_root()
    assert root.name == "cv-ai-engineer-roadmap"