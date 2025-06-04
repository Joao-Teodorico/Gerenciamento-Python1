from pathlib import Path
import pandas as pd

DATA_FILE = Path("data.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    df = pd.read_json(DATA_FILE)
    return df.to_dict(orient="records")
