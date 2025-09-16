import os

from services.api import app

API_KEY = os.getenv("API_KEY", "missing")


@app.get("/config")
def get_config():
    return {"api_key": API_KEY}
