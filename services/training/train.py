from __future__ import annotations

import json
import os
import time
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split

# ========= MLflow setup  =========

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("s3-dev")  # new experiment name


def train_and_save(
    model_path: str = "model/model.joblib",
    max_iter: int = 200,
    test_size: float = 0.2,
    random_state: int = 42,
    cv_folds: int = 5,
) -> dict:
    # 1) Load & explore
    data = load_iris()
    X: np.ndarray = data.data
    y: np.ndarray = data.target
    target_names: list[str] = list(data.target_names)

    print(data.keys())
    print(X.shape)  # features
    print(y.shape)  # labels
    print(data.feature_names)
    print(target_names)

    # 2) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # ---- MLflow: Start a run & log parameters up front ----
    # Keeping run_name helpful for the UI:
    run_name = f"logreg-{int(time.time())}"
    with mlflow.start_run(run_name=run_name) as run:
        # Params we care about (add more if you change solver/penalty later)
        params = {
            "model_type": "LogisticRegression",
            "max_iter": max_iter,
            "test_size": test_size,
            "random_state": random_state,
            "cv_folds": cv_folds,
        }
        mlflow.log_params(params)
        mlflow.set_tags({"stage": "dev", "dataset": "iris"})

        # 3) Train
        model = LogisticRegression(max_iter=max_iter)
        model.fit(X_train, y_train)

        # 4) Evaluate
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"Test set accuracy: {acc:.4f}")

        # Cross-val for robustness
        cv_scores = cross_val_score(LogisticRegression(max_iter=max_iter), X, y, cv=cv_folds)
        cv_mean = float(cv_scores.mean())
        print("Cross-validation scores:", cv_scores)
        print("Mean CV accuracy:", cv_mean)

        # ---- MLflow: Log metrics ----
        mlflow.log_metrics({"accuracy": float(acc), "cv_mean": cv_mean})

        # 5) Save model + metadata (your original)
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        artifact = {
            "model": model,
            "feature_names": data.feature_names,
            "target_names": target_names,
        }
        joblib.dump(artifact, model_path)
        print(f" Saved model to {model_path}")

        # ---- MLflow: Log artifacts (files) ----
        # Save params/metrics as JSON for easier browsing
        Path("artifacts").mkdir(exist_ok=True)
        with open("artifacts/params.json", "w") as f:
            json.dump(params, f, indent=2)
        with open("artifacts/metrics.json", "w") as f:
            json.dump({"accuracy": float(acc), "cv_mean": cv_mean}, f, indent=2)

        # Log all three: params.json, metrics.json, and the joblib model
        mlflow.log_artifact("artifacts/params.json")
        mlflow.log_artifact("artifacts/metrics.json")
        mlflow.log_artifact(model_path, artifact_path="model_joblib")

        # ---- MLflow: (Bonus) log sklearn model in MLflow format ----
        # This creates an MLmodel with environment files for reproducibility.
        try:
            mlflow.sklearn.log_model(sk_model=model, artifact_path="model_sklearn")
        except Exception as e:
            print(f"[MLflow] sklearn log_model skipped: {e}")

        # Optional: print run info for quick copy/paste
        print(f"[MLflow] run_id={run.info.run_id}")
        print(f"[MLflow] artifact_uri={mlflow.get_artifact_uri()}")

        # 6) Sanity check load (kept from your original)
        loaded = joblib.load(model_path)
        print(
            "Sanity check prediction (class index):",
            loaded["model"].predict([X_test[0]])[0],
        )

        return {"accuracy": float(acc), "cv_mean": cv_mean}


if __name__ == "__main__":
    train_and_save()
