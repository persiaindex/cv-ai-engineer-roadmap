from pathlib import Path
import json
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]



def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)



def main() -> None:
    config_path = PROJECT_ROOT / "configs" / "inspection_ai_flow.json"
    config = load_json(config_path)

    benchmark_report_path = PROJECT_ROOT / config["benchmark_report"]
    benchmark_report = load_json(benchmark_report_path)

    project_report = {
        "project_name": "inspection_ai_flow",
        "backend_predict_endpoint_example": config["backend_predict_endpoint_example"],
        "ml_service_predict_endpoint": config["ml_service_predict_endpoint"],
        "ml_service_health_endpoint": config["ml_service_health_endpoint"],
        "benchmark_report_exists": benchmark_report_path.exists(),
        "ml_service_device": benchmark_report["device"],
        "batch_1_throughput": benchmark_report["batch_1"]["throughput_samples_per_second"],
        "batch_4_throughput": benchmark_report["batch_4"]["throughput_samples_per_second"],
        "feature_summary": [
            "inspection defect_score",
            "is_defective flag",
            "is_review flag",
            "is_ok flag"
        ],
        "stored_output_model": "MLPrediction",
        "connected_services": ["django_api", "fastapi_ml_service"],
    }

    project_report_path = PROJECT_ROOT / config["project_report"]
    project_report_path.parent.mkdir(parents=True, exist_ok=True)
    with project_report_path.open("w", encoding="utf-8") as file:
        json.dump(project_report, file, indent=2)

    print(f"Project report created: {project_report_path}")
    print(f"ML service device: {project_report['ml_service_device']}")
    print(f"Batch 1 throughput: {project_report['batch_1_throughput']:.2f}")
    print(f"Batch 4 throughput: {project_report['batch_4_throughput']:.2f}")
    print(f"Stored output model: {project_report['stored_output_model']}")


if __name__ == "__main__":
    main()