from __future__ import annotations

import os
from typing import Final, Optional

from dotenv import load_dotenv

load_dotenv()  # reads .env in project root, if present

API_KEY: Optional[str] = os.getenv("API_KEY")
MODEL_PATH: Final[str] = os.getenv("MODEL_PATH", "model/model.joblib")
