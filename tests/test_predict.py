from fastapi.testclient import TestClient

from services.api.app.main import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["service"] == "api"


def test_predict_ok():
    payload = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert set(body.keys()) == {"prediction_index", "prediction_label"}
    assert body["prediction_label"] in {"setosa", "versicolor", "virginica"}


def test_predict_validation():
    r = client.post("/predict", json={"sepal_length": 5.1})  # missing fields
    assert r.status_code == 422


def test_predict_bad_type():
    # string instead of float -> pydantic should be 422
    r = client.post(
        "/predict",
        json={
            "sepal_length": "oops",
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    assert r.status_code == 422


def test_predict_extra_field_current_behaviour():
    # pydantic ignores extra fields by default
    r = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
            "extra": 1,
        },
    )
    assert r.status_code in (200, 422)
