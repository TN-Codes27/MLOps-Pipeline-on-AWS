from __future__ import annotations

import os
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def train_and_save(model_path: str = "model/model.joblib") -> dict:
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
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 3) Train
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # 4) Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test set accuracy: {acc:.2f}")

    # Cross-val for robustness
    cv_scores = cross_val_score(LogisticRegression(max_iter=200), X, y, cv=5)
    print("Cross-validation scores:", cv_scores)
    print("Mean CV accuracy:", cv_scores.mean())

    # 5) Save model + metadata
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    artifact = {
        "model": model,
        "feature_names": data.feature_names,
        "target_names": target_names,
    }
    joblib.dump(artifact, model_path)
    print(f" Saved model to {model_path}")

    # 6) Sanity check load
    loaded = joblib.load(model_path)
    print("Sanity check prediction (class index):", loaded["model"].predict([X_test[0]])[0])

    return {"accuracy": acc, "cv_mean": float(cv_scores.mean())}


if __name__ == "__main__":
    train_and_save()
