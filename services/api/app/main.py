import os
from typing import Any, List

import joblib
import numpy as np
from fastapi import FastAPI, HTTPException

from .schemas import PredictIn, PredictOut

app = FastAPI(title="mlops-api", version="0.1.0")

LABELS: List[str] = ["setosa", "versicolor", "virginica"]

try:
    _loaded: Any = joblib.load("model/model.joblib")
    if isinstance(_loaded, dict):
        model = _loaded["model"]
        # If training saved names, prefer them
        if "target_names" in _loaded and isinstance(_loaded["target_names"], (list, tuple)):
            LABELS = list(_loaded["target_names"])
    else:
        model = _loaded
except Exception as e:
    raise RuntimeError(f"Could not load model: {e}") from e


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "api", "version": "0.1.0"}


@app.post("/predict", response_model=PredictOut)
def predict(payload: PredictIn) -> PredictOut:
    try:
        X = np.array(
            [
                [
                    payload.sepal_length,
                    payload.sepal_width,
                    payload.petal_length,
                    payload.petal_width,
                ]
            ],
            dtype=float,
        )
        idx = int(model.predict(X)[0])
        if not (0 <= idx < len(LABELS)):
            raise ValueError(f"class index {idx} out of range")
        return PredictOut(prediction_index=idx, prediction_label=LABELS[idx])

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {e}")


@app.get("/force-500")
def force_500() -> dict[str, str]:
    # Deliberately create a server error for monitoring tests
    raise HTTPException(status_code=500, detail="forced 500 for monitoring test")


@app.get("/version")
def version() -> dict[str, str]:
    return {"git_sha": os.getenv("GIT_SHA", "dev")}
