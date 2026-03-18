from pathlib import Path
import json

import torch
from PIL import Image, ImageDraw
from torchvision import models, transforms


COCO_LABELS = {
    1: "person",
    2: "bicycle",
    3: "car",
    4: "motorcycle",
    5: "airplane",
    6: "bus",
    7: "train",
    8: "truck",
    9: "boat",
    10: "traffic light",
    11: "fire hydrant",
    13: "stop sign",
    14: "parking meter",
    15: "bench",
    16: "bird",
    17: "cat",
    18: "dog",
    19: "horse",
    20: "sheep",
    21: "cow",
    22: "elephant",
    23: "bear",
    24: "zebra",
    25: "giraffe",
    27: "backpack",
    28: "umbrella",
    31: "handbag",
    32: "tie",
    33: "suitcase",
    34: "frisbee",
    35: "skis",
    36: "snowboard",
    37: "sports ball",
    38: "kite",
    39: "baseball bat",
    40: "baseball glove",
    41: "skateboard",
    42: "surfboard",
    43: "tennis racket",
    44: "bottle",
    46: "wine glass",
    47: "cup",
    48: "fork",
    49: "knife",
    50: "spoon",
    51: "bowl",
    52: "banana",
    53: "apple",
    54: "sandwich",
    55: "orange",
    56: "broccoli",
    57: "carrot",
    58: "hot dog",
    59: "pizza",
    60: "donut",
    61: "cake",
    62: "chair",
    63: "couch",
    64: "potted plant",
    65: "bed",
    67: "dining table",
    70: "toilet",
    72: "tv",
    73: "laptop",
    74: "mouse",
    75: "remote",
    76: "keyboard",
    77: "cell phone",
    78: "microwave",
    79: "oven",
    80: "toaster",
    81: "sink",
    82: "refrigerator",
    84: "book",
    85: "clock",
    86: "vase",
    87: "scissors",
    88: "teddy bear",
    89: "hair drier",
    90: "toothbrush",
}



def load_detector() -> torch.nn.Module:
    model = models.detection.ssdlite320_mobilenet_v3_large(
        weights=models.detection.SSDLite320_MobileNet_V3_Large_Weights.DEFAULT
    )
    model.eval()
    return model



def load_image_tensor(image_path: Path) -> tuple[Image.Image, torch.Tensor]:
    image = Image.open(image_path).convert("RGB")
    tensor = transforms.ToTensor()(image)
    return image, tensor



def run_detection(image_path: Path, score_threshold: float = 0.4) -> list[dict]:
    model = load_detector()
    image, tensor = load_image_tensor(image_path)

    with torch.no_grad():
        predictions = model([tensor])[0]

    detections: list[dict] = []

    for box, score, label in zip(predictions["boxes"], predictions["scores"], predictions["labels"]):
        score_value = float(score.item())
        if score_value < score_threshold:
            continue

        label_id = int(label.item())
        label_name = COCO_LABELS.get(label_id, f"class_{label_id}")
        x1, y1, x2, y2 = [float(v) for v in box.tolist()]

        detections.append(
            {
                "label_id": label_id,
                "label_name": label_name,
                "score": score_value,
                "box": [x1, y1, x2, y2],
                "image_size": list(image.size),
            }
        )

    return detections



def draw_detections(image_path: Path, detections: list[dict], output_path: Path) -> None:
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)

    for detection in detections:
        x1, y1, x2, y2 = detection["box"]
        label = detection["label_name"]
        score = detection["score"]
        draw.rectangle([x1, y1, x2, y2], outline="red", width=3)
        draw.text((x1, max(0, y1 - 12)), f"{label} {score:.2f}", fill="red")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)



def save_detection_json(output_path: Path, image_path: Path, detections: list[dict]) -> None:
    report = {
        "image_path": str(image_path),
        "detection_count": len(detections),
        "detections": detections,
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)