# Inspection Detection Baseline

## Purpose
This mini project is a CPU-friendly detection baseline for industrial inspection learning.

## What It Combines
- pretrained detector inference
- saved annotated detection output
- IoU, NMS, precision, and recall basics
- tiny fine-tuning strategy package
- ONNX export and benchmark preparation

## Main Inputs
- `data/detection/input/sample_scene.jpg`
- `artifacts/detection/detection_metrics_report.json`
- `artifacts/detection/fine_tune_strategy_report.json`
- `artifacts/onnx/onnx_benchmark_report.json`

## Main Outputs
- annotated detection image
- detection JSON output
- project summary report in `projects/inspection_detection_baseline/output/`

## Current Limits
- pretrained general detector, not a defect-specific model
- tiny dataset for fine-tuning readiness only
- CPU-first workflow

## Why This Matters
This project shows a practical object-detection engineering workflow before full detector fine-tuning.