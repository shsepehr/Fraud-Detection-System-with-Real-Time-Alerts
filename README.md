# 🚨 Fraud Detection System with Real-Time Alerts

A production-ready system for detecting fraudulent financial transactions using Machine Learning, FastAPI, and Streamlit.  
This project simulates a real-world FinTech pipeline: training a fraud model, serving predictions via API, and real-time dashboard alerts.

---

## ⭐ Features
- 🧠 ML Model (Isolation Forest)
- ⚡ REST API with FastAPI
- 📊 Real-time dashboard (Streamlit)
- 🗂️ Modular project structure (Production-friendly)
- 💾 Sample dataset included
- 🚀 Easy to deploy & extend

---

## 📂 Project Structure
fraud-detection-system/
├── data/ # dataset
├── model/ # training & saved model
├── app/ # API + dashboard
└── requirements.txt


---

## 🔧 Installation
```bash
cd fraud-detection-system
pip install -r requirements.txt
---
⚙️ Train the Model
python model/train_model.py

---
Run the API
uvicorn app.api:app --reload
---
Run Dashboard
streamlit run app/streamlit_dashboard.py

