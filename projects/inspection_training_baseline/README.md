# Inspection Training Baseline

## Purpose
This mini project is a CPU-friendly image classification training baseline for simple industrial inspection.

## What It Uses
- PyTorch
- torchvision `ImageFolder`
- transfer learning with ResNet18
- train and validation loops
- checkpoint saving
- evaluation report generation

## Dataset
- `data/datasets/inspection_cls`
- classes: `ok`, `defect`

## Outputs
- model checkpoint in `artifacts/`
- evaluation outputs in `artifacts/evaluation/`
- project summary report in `projects/inspection_training_baseline/output/`

## Current Limits
- very small synthetic dataset
- CPU-only training
- short demonstration training run

## Why This Matters
This project shows a full small training workflow with reproducible code, saved artifacts, and evaluation outputs.