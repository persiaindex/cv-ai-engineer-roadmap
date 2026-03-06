from pathlib import Path
import platform
import sys

import numpy as np
import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]

    print("Environment check")
    print("=" * 30)
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Operating system: {platform.system()} {platform.release()}")
    print(f"Project root: {project_root}")
    print(f"NumPy version: {np.__version__}")
    print(f"Pandas version: {pd.__version__}")

if __name__ == "__main__":
    main()