# Inspection Dataset v1

## Purpose
This dataset is a small synthetic starter dataset for industrial inspection experiments.

## Task
Binary image classification:
- `ok`
- `defect`

## Folder Structure
- `images/` contains the image files
- `labels.csv` contains labels and split information

## Label Meaning
- `ok` means no visible defect in the image
- `defect` means at least one visible defect is present

## Current Size
- 2 images
- 2 labeled rows

## Known Limits
- very small
- synthetic only
- not enough for real model training yet

## Next Improvements
- add more examples
- create validation and test splits
- add bounding boxes later if object detection is needed