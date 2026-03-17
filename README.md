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

## Day 9 status
- [X] models added in `apps/api/core/models.py`
- [X] admin registration in `apps/api/core/admin.py`
- [X] migrations created and applied
- [X] sample objects created in Django admin
- [X] notes in `docs/day09_notes.md`

## Day 10 status
- [X] model tests added
- [X] fixture file added
- [X] `python manage.py test` passes
- [X] fixture loads successfully
- [X] sample data visible in admin
- [X] notes in `docs/day10_notes.md`

## Day 11 status
- [X] DRF installed
- [X] serializers added
- [X] viewsets added
- [X] API routes working
- [X] JSON endpoints visible in browser
- [X] notes in `docs/day11_notes.md`

## Day 12 status
- [X] `django-filter` installed
- [X] pagination enabled
- [X] filters/search/ordering enabled
- [X] validation rules added
- [X] test URLs working
- [X] notes in `docs/day12_notes.md`

## Day 13 status
- [X] JWT package installed
- [X] token routes added
- [X] API read access works without login
- [X] write access is blocked without login
- [X] token endpoint works

## Day 14 status
- [X] `drf-spectacular` installed
- [X] `core/exceptions.py` added
- [X] custom error format working
- [X] schema endpoint working
- [X] Swagger and ReDoc pages working
- [X] notes in `docs/day14_notes.md`

## Day 15 status
- [X] `core/services.py` added
- [X] dashboard summary endpoint works
- [X] alert close endpoint works
- [X] API tests added in `tests_api.py`
- [X] notes in `docs/day15_notes.md`

## Day 16 status
- [X] `apps/web` created with Vite React TypeScript
- [X] frontend runs in browser
- [X] starter page replaced
- [X] optional first reusable component added
- [X] notes in `docs/day16_notes.md`

## Day 17 status
- [X] reusable components added
- [X] mock data added
- [X] `useState` used at least once
- [X] machine and alert sections rendered
- [X] notes in `docs/day17_notes.md`

## Day 18 status
- [X] `MachineForm.tsx` added
- [X] form state works
- [X] validation messages work
- [X] success message works
- [X] notes in `docs/day18_notes.md`

## Day 19 status
- [X] routing added
- [X] table component added
- [X] chart component added
- [X] dashboard page created
- [X] machines page created
- [X] notes in `docs/day19_notes.md`

## Day 20 status
- [X] `axios` installed
- [X] `lib/api.ts` added
- [X] `hooks/useMachines.ts` added
- [X] Machines page connected to Django
- [X] loading state works
- [X] error state works
- [X] notes in `docs/day20_notes.md`

## Day 21 status
- [X] `types/machine.ts` added
- [X] `lib/mappers.ts` added
- [X] `ApiMessage.tsx` added
- [X] `useMachines.ts` cleaned up
- [X] `MachinesPage.tsx` cleaned up
- [X] notes in `docs/day21_notes.md`

## Day 22 status
- [X] `apps/api/Dockerfile` added
- [X] `apps/web/Dockerfile` added
- [X] `.dockerignore` files added
- [X] backend image builds and runs
- [X] frontend image builds and runs
- [X] notes in `docs/day22_notes.md`

## Day 23 status
- [X] `docker-compose.yml` added
- [X] `apps/api/.env.docker` added
- [X] PostgreSQL driver installed
- [X] Django configured for PostgreSQL
- [X] full stack starts with Compose
- [X] migrations run inside the container
- [X] frontend and backend open in the browser
- [X] notes in `docs/day23_notes.md`

## Day 24 status
- [X] `apps/api/.env.example` added
- [X] `apps/web/.env.example` added
- [X] `python-dotenv` installed
- [X] Django settings read from `.env`
- [X] frontend API URL reads from `VITE_API_BASE_URL`
- [X] `.gitignore` handles `.env` files correctly
- [X] notes in `docs/day24_notes.md`

## Day 25 status
- [X] `types/dashboard.ts` added
- [X] `hooks/useDashboardSummary.ts` added
- [X] `hooks/useAlerts.ts` added
- [X] `SummaryCards.tsx` added
- [X] dashboard uses real API data
- [X] alerts list uses real API data
- [X] chart uses real API data
- [X] notes in `docs/day25_notes.md`

## Day 26 status
- [X] `src/cv/cv_utils.py` added
- [X] `src/cv/main.py` added
- [X] `scripts/run_cv.py` added
- [X] `tests/test_cv.py` added
- [X] sample input and output images created
- [X] notes in `docs/day26_notes.md`

## Day 27 status
- [X] `src/cv/inspection.py` added
- [X] `scripts/run_inspection.py` added
- [X] `tests/test_inspection.py` added
- [X] inspection debug images created
- [X] notes in `docs/day27_notes.md`

## Day 28 status
- [X] `data/datasets/inspection_v1/labels.csv` added
- [X] `data/datasets/inspection_v1/dataset_card.md` added
- [X] `src/cv/dataset_utils.py` added
- [X] `scripts/build_dataset_manifest.py` added
- [X] `tests/test_dataset_manifest.py` added
- [X] `manifest.json` created
- [X] notes in `docs/day28_notes.md`

## Day 29 status
- [X] `configs/inspection_config.json` added
- [X] `src/cv/pipeline.py` added
- [X] `scripts/run_inspection_config.py` added
- [X] `tests/test_pipeline.py` added
- [X] config-driven output images created
- [X] notes in `docs/day29_notes.md`

## Day 30 status
- [X] `projects/pcb_defect_baseline/README.md` added
- [X] `scripts/run_pcb_baseline.py` added
- [X] `tests/test_pcb_baseline.py` added
- [X] `baseline_report.json` created
- [X] annotated baseline outputs created
- [X] notes in `docs/day30_notes.md`

## Day 31 status
- [X] `src/ml/dataset.py` added
- [X] `src/ml/model.py` added
- [X] `src/ml/train_demo.py` added
- [X] `scripts/run_torch_demo.py` added
- [X] `tests/test_torch_demo.py` added
- [X] notes in `docs/day31_notes.md`

## Day 32 status
- [X] `src/ml/trainer.py` added
- [X] `scripts/run_training_loop.py` added
- [X] `tests/test_trainer.py` added
- [X] checkpoint file created
- [X] notes in `docs/day32_notes.md`

## Day 33 status
- [X] `src/ml/transfer_learning.py` added
- [X] `scripts/run_transfer_learning.py` added
- [X] `tests/test_transfer_learning.py` added
- [X] `inspection_cls` dataset folders created
- [X] checkpoint file created
- [X] notes in `docs/day33_notes.md`