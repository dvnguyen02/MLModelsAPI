# ML Model Deployment with FastAPI

## Overview
This project demonstrates deploying a machine learning model (Random Forest Classifier trained on Iris dataset) using FastAPI and Docker.

## Components
- `classification_task.py`: Model training script
- `server.py`: FastAPI server for model predictions
- `client.py`: Example client to test model predictions
- `Dockerfile`: Containerization configuration

## Quick Start
1. Train the model: `python classification_task.py`
2. Run the server: `uvicorn server:app --host 0.0.0.0 --port 5000`
3. Test predictions using `client.py`

## Docker Deployment
```bash
docker build -t ml-iris-api .
docker run -p 5000:5000 ml-iris-api
```

## Dependencies
- scikit-learn
- fastapi
- uvicorn
