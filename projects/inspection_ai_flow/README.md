# Inspection AI Flow

## Purpose
This mini project demonstrates an end-to-end AI-assisted inspection workflow.

## What It Connects
- Django backend inspection records
- FastAPI ML inference service
- saved prediction results in the database
- prediction endpoint in the backend API
- benchmarked ML service artifacts

## Main Workflow
1. an inspection exists in Django
2. Django sends features to the ML service
3. the ML service returns a class and probabilities
4. Django stores the prediction as an `MLPrediction`
5. the API returns the saved prediction result

## Main Inputs
- inspection records in Django
- ML service endpoint `/predict`
- backend endpoint `/api/inspections/<id>/predict/`

## Main Outputs
- saved `MLPrediction` database rows
- API prediction responses
- project summary report in `projects/inspection_ai_flow/output/`

## Why This Matters
This project shows that the model is no longer only a demo. It is now part of a backend workflow that behaves like a real feature.