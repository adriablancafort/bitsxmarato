from db import Database
import random
import pandas as pd
from datetime import datetime, date
import numpy as np

db = Database()
responses = db.db["responses"]

def generate_symptom_data():
    # Define symptoms and their trend parameters
    simptoms = {
        "diarrea": {"amplitude": 10, "phase_shift": 0, "trend": -0.02},
        "esgotament": {"amplitude": 8, "phase_shift": 1, "trend": 0.05},
        "mal_de_cap": {"amplitude": 6, "phase_shift": 2, "trend": 0.02},
        "mal_de_coll": {"amplitude": 7, "phase_shift": 3, "trend": -0.01},
        "mal_de_panxa": {"amplitude": 5, "phase_shift": 4, "trend": 0},
        "mocs": {"amplitude": 12, "phase_shift": 0, "trend": 0.03},
        "tos": {"amplitude": 9, "phase_shift": 1, "trend": -0.02},
        "vomits": {"amplitude": 4, "phase_shift": 2, "trend": 0.01},
        "altres": {"amplitude": 6, "phase_shift": 3, "trend": 0.04},
    }

    # Generate daily timestamps for a year
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    date_range = pd.date_range(start=start_date, end=end_date, freq="D")

    # Create records
    records = []
    for date_idx, date in enumerate(date_range):
        for simptom, params in simptoms.items():
            # Generate seasonal and trend components
            seasonality = params["amplitude"] * np.sin((2 * np.pi * date_idx / 365) + params["phase_shift"])
            trend = params["trend"] * date_idx
            count = max(0, int(seasonality + trend))  # Ensure non-negative
            if count > 0:  # Only include records with non-zero count
                records.append({
                    "timestamp": date,
                    "simptom": simptom,
                    "count": count
                })

    # Convert to DataFrame
    return pd.DataFrame(records)

data = generate_symptom_data()

for _, row in data.iterrows():
    responses.insert_one(row.to_dict())
