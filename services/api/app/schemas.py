from pydantic import BaseModel, Field, ConfigDict

class PredictIn(BaseModel):
    sepal_length: float = Field(description="Length of the sepal")
    sepal_width: float = Field(description="Width of the sepal")
    petal_length: float = Field(description="Length of the petal")
    petal_width: float = Field(description="Width of the petal")

    model_config = ConfigDict(populate_by_name=True, extra="forbid")

class PredictOut(BaseModel):
    prediction_index: int
    prediction_label: str

 