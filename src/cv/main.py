from pathlib import Path

import cv2
import numpy as np

from cv.cv_utils import convert_to_rgb, draw_label, load_image, resize_image, save_image


def create_sample_image(path: Path) -> None:
    image = np.zeros((240, 320, 3), dtype=np.uint8)
    image[:] = (40, 40, 40)
    cv2.rectangle(image, (60, 60), (260, 180), (0, 255, 0), 2)
    cv2.circle(image, (160, 120), 25, (255, 0, 0), -1)
    cv2.putText(image, "Sample", (110, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.imwrite(str(path), image)


def main() -> None:
    project_root = Path(__file__).resolve().parents[2]
    input_path = project_root / "data" / "images" / "sample_input.png"
    output_path = project_root / "data" / "output" / "sample_output.png"

    input_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        create_sample_image(input_path)

    image = load_image(input_path)
    resized = resize_image(image, width=200, height=150)
    rgb_image = convert_to_rgb(resized)
    annotated = draw_label(rgb_image, "OpenCV OK", x=20, y=30)
    save_image(output_path, annotated)

    print(f"Input image shape: {image.shape}")
    print(f"Resized image shape: {resized.shape}")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()