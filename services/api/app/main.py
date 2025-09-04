from fastapi import FastAPI
from schemas import PredictIn, PredictOut

app = FastAPI(title="mlops-api", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "api", "version": "0.1.0"}

@app.post("/predict", response_model=PredictOut)
def predict(payload: PredictIn) -> PredictOut: 
    #dummy logic to replace later 
    pred = payload.feature1 * 0.3 + payload.feature2 * 0.7
    return PredictOut (prediction=pred)

