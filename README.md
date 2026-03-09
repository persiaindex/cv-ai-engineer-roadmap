# CV AI Engineer Roadmap

This repository documents my 16-week employment-first roadmap toward Applied AI / Computer Vision Engineering in Germany.

## Goals
- Build production-style AI software
- Learn Python backend, React frontend, REST APIs, Docker, and computer vision
- Create a strong portfolio for industrial AI roles

## Planned architecture
- `apps/api` - Django backend
- `apps/web` - React frontend
- `apps/ml_service` - FastAPI inference service
- `apps/sim_service` - simulation service

## Environment
- Windows
- Python 3.x
- Node.js LTS
- Docker Desktop

## Day 1 status
- [x] Tools installed
- [x] Repo created
- [x] Virtual environment created
- [x] Initial script added

## Day 2 status
- [x] `src/core` package created
- [x] `paths.py`, `config.py`, `logger.py`, and `main.py` added
- [x] `app.json` and `app.yaml` created
- [x] `python scripts/run_core.py` works
- [x] first test passes
- [x] changes committed and pushed to GitHub

## Day 3 status
- [x] `src/domain` package created
- [x] machine, feeder, inspection, and alert classes added
- [x] `python scripts/run_domain.py` works
- [x] domain tests pass
- [x] changes committed and pushed to GitHub

## Day 4 status
- [x] `src/vision` package created
- [x] image and signal utilities added
- [x] `python scripts/run_vision.py` works
- [x] vision tests pass
- [x] changes committed and pushed to GitHub

## Day 5 status
- [] 

## Day 6 status
- [X] PostgreSQL container is running
- [X] schema file created
- [X] seed file created
- [X] query file created
- [X] tables created successfully
- [X] sample data inserted
- [X] select/update/delete queries tested
- [X] notes written in `docs/day06_notes.md`
- [X] changes committed and pushed

## Day 7 status
- [X] JOIN combines related tables
- [X] GROUP BY creates KPIs
- [X] CASE turns raw values into business labels
- [X] WITH creates readable intermediate query steps
- [X] ROW_NUMBER() helps select the latest row per machine

## Day 8 status
- [X] `apps/api/config/`
- [X] `apps/api/core/`
- [X] Django installed in `requirements.txt`
- [X] initial migrations applied
- [X] admin login working
- [X] notes in `docs/day08_notes.md`