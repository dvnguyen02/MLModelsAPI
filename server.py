from fastapi import FastAPI
import pickle

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

class_names = ['Setosa', 'Versicolor', 'Virginica']
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ML Model API"}
@app.post("/predict")
def predict(data: dict):
    prediction = model.predict([data["features"]])[0]
    class_name = class_names[prediction]
    return {"prediction": class_name}