# AI381 Lab 2 – Machine Learning Operations

**Course:** AI381 – Machine Learning Operations  
**Instructor:** Dr. Tariq Al-Omari  
**University:** Jordan University of Science and Technology (JUST)  
**Semester:** Fall 2026/27

[![CI](https://github.com/sallyalhamdan/AI381-Lab2/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/sallyalhamdan/AI381-Lab2/actions/workflows/ci.yml)

## Project Overview

This project demonstrates an end-to-end Machine Learning Operations (MLOps) workflow. It packages a machine learning model behind a FastAPI service, validates the API using automated tests, containerizes the application with Docker, and automates quality checks and image publishing using GitHub Actions.

## Technologies Used

- Python 3.13
- FastAPI and Uvicorn
- Scikit-learn, Pandas, and Joblib
- Pytest for automated testing
- Ruff for code linting
- Docker with a multi-stage build
- GitHub Actions for CI/CD
- Trivy for container vulnerability scanning
- GitHub Container Registry (GHCR) for Docker image publishing

## Project Structure

```text
AI381-Lab2/
├── app/
│   └── main.py
├── src/
├── tests/
├── model.joblib
├── requirements.txt
├── Dockerfile
└── README.md
```

## Installation and Local Setup

Clone the repository:

```bash
git clone https://github.com/sallyalhamdan/AI381-Lab2.git
cd AI381-Lab2
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install pytest ruff
```

## Run the Application

Start the FastAPI service with one command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The API will be available at:

- **Health Check:** http://localhost:8000/health
- **API Documentation:** http://localhost:8000/docs
- **Prediction Endpoint:** http://localhost:8000/predict

## Automated Tests

The project includes five automated tests using Pytest:

1. **Health Endpoint Test:** Verifies that `/health` returns HTTP 200 and the expected status.
2. **Prediction Endpoint Test:** Checks that `/predict` accepts valid customer data and returns a churn probability.
3. **Probability Range Test:** Ensures the predicted probability is between 0 and 1.
4. **Deterministic Prediction Test:** Verifies that identical inputs produce identical predictions.
5. **Invalid Input Test:** Checks that invalid input is rejected by the API.

Run the tests:

```bash
pytest -v
```

Run code quality checks:

```bash
ruff check src
```

## Docker

Build the Docker image:

```bash
docker build -t ai381-lab2 .
```

Run the container:

```bash
docker run -d --name ai381-lab2-container -p 8000:8000 ai381-lab2
```

The Docker image uses a multi-stage build, runs the application as a non-root user, and includes a health check for the `/health` endpoint.

## CI/CD Pipeline

GitHub Actions automatically runs linting and automated tests on pushes and pull requests targeting the `main` branch.

When changes are pushed to `main`, the workflow:

1. Runs linting and automated tests.
2. Builds the Docker image.
3. Scans the image for vulnerabilities using Trivy.
4. Publishes the Docker image to GitHub Container Registry (GHCR), tagged with the Git commit SHA.

All third-party GitHub Actions are pinned to full commit SHAs.

## Docker Image

The published image is available through GitHub Container Registry:

```text
ghcr.io/sallyalhamdan/ai381-lab2
```

### Latest Published Image

- **Image:** `ghcr.io/sallyalhamdan/ai381-lab2`
- **Tag:** `d51d23c4b80f3f96831f3dbf5c85659473c80d73`
- **Digest:** `sha256:bad1d5e6cf915cd10a8b466460b32a7b4ae9d367020fe2524b88a36eaaf08ecc`

Pull the latest published image:

```bash
docker pull ghcr.io/sallyalhamdan/ai381-lab2:d51d23c4b80f3f96831f3dbf5c85659473c80d73
```

Run the published image:

```bash
docker run -d --name ai381-lab2-container -p 8000:8000 ghcr.io/sallyalhamdan/ai381-lab2:d51d23c4b80f3f96831f3dbf5c85659473c80d73
```

## Branch Protection

The `main` branch is protected with the following requirements:

- Pull requests are required before merging.
- The `lint-and-test` status check must pass before merging.
- Force pushes are disabled.
- Branch deletion is disabled.

## Repository

[AI381-Lab2 – GitHub](https://github.com/sallyalhamdan/AI381-Lab2)
