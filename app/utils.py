import joblib
import os
import pandas as pd
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from model.train_model import train_model

MODEL_PATH = "model/model.pkl"
LE_LOCATION_PATH = "model/le_location.pkl"
LE_CARD_PATH = "model/le_card.pkl"

def load_model():
    if not os.path.exists(MODEL_PATH):
        print("⚠️ model.pkl not found — training model...")
        train_model()
        print("✅ Model trained and saved!")
    model = joblib.load(MODEL_PATH)
    le_location = joblib.load(LE_LOCATION_PATH)
    le_card = joblib.load(LE_CARD_PATH)
    return model, le_location, le_card

def safe_encode(encoder, value):
    """ اگر مقدار جدید بود => Unknown و ساخت رمز """
    if value not in encoder.classes_:
        encoder.classes_ = list(encoder.classes_) + [value]
    return encoder.transform([value])[0]

def predict_fraud(amount, location, card_type):
    model, le_location, le_card = load_model()

    location_enc = safe_encode(le_location, location)
    card_enc = safe_encode(le_card, card_type)

    X = pd.DataFrame([[amount, location_enc, card_enc]], 
        columns=['amount', 'location_enc', 'card_type_enc']
    )

    pred = model.predict(X)
    return "Fraudulent ⚠️" if pred[0] == 1 else "Legit ✅"
