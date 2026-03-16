from pathlib import Path

import cv2
import numpy as np



def create_inspection_sample(path: Path) -> None:
    image = np.full((240, 320, 3), 220, dtype=np.uint8)

    cv2.rectangle(image, (40, 50), (280, 190), (180, 180, 180), -1)
    cv2.circle(image, (120, 120), 18, (20, 20, 20), -1)
    cv2.rectangle(image, (200, 90), (230, 120), (30, 30, 30), -1)

    cv2.imwrite(str(path), image)



def to_grayscale(image: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



def threshold_defects(gray: np.ndarray) -> np.ndarray:
    _, mask = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)
    return mask



def clean_mask(mask: np.ndarray) -> np.ndarray:
    kernel = np.ones((3, 3), np.uint8)
    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    return cleaned



def find_defect_contours(mask: np.ndarray) -> list[np.ndarray]:
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours



def draw_defect_boxes(image: np.ndarray, contours: list[np.ndarray], min_area: int = 50) -> np.ndarray:
    output = image.copy()

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(output, f"area={int(area)}", (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    return output