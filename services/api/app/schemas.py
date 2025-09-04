from pydantic import BaseModel

class PredictIn(BaseModel):
    feature1: float
    feature2: float

class PredictOut(BaseModel):
    prediction: float