from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

from ml.train_demo import run_training_demo


if __name__ == "__main__":
    result = run_training_demo()
    print(f"Batch shape: {result['batch_shape']}")
    print(f"Logits shape: {result['logits_shape']}")
    print(f"Loss before step: {result['loss_before']:.6f}")
    print(f"Loss after step: {result['loss_after']:.6f}")