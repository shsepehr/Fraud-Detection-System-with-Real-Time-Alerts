from fastapi import FastAPI
from pydantic import BaseModel
from .utils import predict_fraud

app = FastAPI(title="Fraud Detection API")

class Transaction(BaseModel):
    amount: float
    location: str
    card_type: str

@app.get("/")
def home():
    return {"message": "Fraud Detection API running"}

@app.post("/predict")
def predict(transaction: Transaction):
    result = predict_fraud(transaction.amount, transaction.location, transaction.card_type)
    return {"prediction": result}
