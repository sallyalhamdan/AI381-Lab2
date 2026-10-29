import sys
from pathlib import Path

from fastapi.testclient import TestClient

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

from app.main import app
client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    customer = {
        "tenure_months": 72,
        "monthly_charges": 45.0,
        "contract": "two-year",
        "internet_service": "dsl",
        "support_calls": 1,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200
    assert "churn_probability" in response.json()


def test_predict_probability_range():
    customer = {
        "tenure_months": 72,
        "monthly_charges": 45.0,
        "contract": "two-year",
        "internet_service": "dsl",
        "support_calls": 1,
    }

    response = client.post("/predict", json=customer)

    assert response.status_code == 200
    probability = response.json()["churn_probability"]
    assert 0 <= probability <= 1


def test_predict_is_deterministic():
    customer = {
        "tenure_months": 72,
        "monthly_charges": 45.0,
        "contract": "two-year",
        "internet_service": "dsl",
        "support_calls": 1,
    }

    first = client.post("/predict", json=customer)
    second = client.post("/predict", json=customer)

    assert first.status_code == 200
    assert second.status_code == 200
    assert first.json() == second.json()


def test_invalid_input():
    response = client.post("/predict", json={})

    assert response.status_code in (400, 422)