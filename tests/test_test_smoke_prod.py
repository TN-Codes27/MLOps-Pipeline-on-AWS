import os

import pytest
import requests

ALB = os.getenv("ALB_URL")


@pytest.mark.skipif(not ALB, reason="ALB_URL not set")
def test_prod_health():
    r = requests.get(f"{ALB}/health", timeout=5)
    assert r.status_code == 200
