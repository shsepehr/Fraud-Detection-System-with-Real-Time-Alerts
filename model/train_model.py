import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

MODEL_PATH = "model/model.pkl"

def train_model():
    os.makedirs("model", exist_ok=True)

    df = pd.read_csv("data/transactions.csv")

    # Encode categorical features
    le_location = LabelEncoder()
    le_card = LabelEncoder()
    df['location_enc'] = le_location.fit_transform(df['location'])
    df['card_type_enc'] = le_card.fit_transform(df['card_type'])

    # Save encoders
    joblib.dump(le_location, "model/le_location.pkl")
    joblib.dump(le_card, "model/le_card.pkl")

    # Features and target
    X = df[['amount', 'location_enc', 'card_type_enc']]
    y = df['is_fraud']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, MODEL_PATH)
    print(f"🎉 Model trained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
