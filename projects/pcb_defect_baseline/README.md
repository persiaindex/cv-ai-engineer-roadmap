# PCB Defect Baseline

## Purpose
This mini project is a CPU-friendly classical computer vision baseline for simple industrial defect inspection.

## What It Uses
- OpenCV preprocessing
- thresholding
- morphology
- contour detection
- dataset manifest generation

## Inputs
- images from `data/datasets/inspection_v1/images`
- labels from `data/datasets/inspection_v1/labels.csv`

## Outputs
- annotated images in `projects/pcb_defect_baseline/output`
- `baseline_report.json` with simple summary metrics

## Current Limits
- synthetic dataset
- very small dataset
- classical CV only
- not yet a trained ML model

## Why This Matters
This baseline proves the inspection pipeline before moving to heavier model training.