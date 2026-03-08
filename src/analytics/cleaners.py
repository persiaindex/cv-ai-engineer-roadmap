import pandas as pd


def clean_sensor_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned["timestamp"] = pd.to_datetime(cleaned["timestamp"])
    cleaned["fill_level"] = cleaned["fill_level"].fillna(cleaned["fill_level"].median())
    return cleaned


def clean_inspection_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned["timestamp"] = pd.to_datetime(cleaned["timestamp"])
    cleaned["status"] = cleaned["status"].str.lower().str.strip()
    return cleaned