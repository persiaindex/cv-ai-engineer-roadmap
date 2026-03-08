import pandas as pd


def compute_sensor_kpis(sensor_df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        sensor_df.groupby("machine_id", as_index=False)
        .agg(
            avg_fill_level=("fill_level", "mean"),
            min_fill_level=("fill_level", "min"),
            avg_temperature=("temperature", "mean"),
            max_vibration=("vibration", "max"),
        )
    )
    return summary


def compute_inspection_kpis(inspection_df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        inspection_df.groupby("machine_id", as_index=False)
        .agg(
            inspection_count=("inspection_id", "count"),
            avg_defect_score=("defect_score", "mean"),
        )
    )

    defective_counts = (
        inspection_df.assign(is_defective=inspection_df["status"] == "defective")
        .groupby("machine_id", as_index=False)["is_defective"]
        .sum()
        .rename(columns={"is_defective": "defective_count"})
    )

    return summary.merge(defective_counts, on="machine_id", how="left")


def build_machine_summary(sensor_kpis: pd.DataFrame, inspection_kpis: pd.DataFrame) -> pd.DataFrame:
    summary = sensor_kpis.merge(inspection_kpis, on="machine_id", how="left")
    summary["needs_attention"] = (
        (summary["min_fill_level"] < 20)
        | (summary["max_vibration"] > 0.45)
        | (summary["defective_count"] > 0)
    )
    return summary