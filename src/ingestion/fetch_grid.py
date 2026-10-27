import os
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def fetch_grid_status():
    token = os.getenv("ESKOM_TOKEN")
    if not token:
        return pd.DataFrame([{
            "stage": None,
            "status": "TOKEN_MISSING",
            "fetched_at": datetime.utcnow().isoformat() + "Z"
        }])
    
    headers = {"token": token}
    try:
        response = requests.get("https://developer.sepush.co.za/business/2.0/status", headers=headers, timeout=30)
        data = response.json()
        stage = data.get("status", {}).get("eskom", {}).get("stage")
        return pd.DataFrame([{
            "stage": stage,
            "status": "OK",
            "fetched_at": datetime.utcnow().isoformat() + "Z"
        }])
    except Exception as e:
        return pd.DataFrame([{
            "stage": None,
            "status": "ERROR",
            "fetched_at": datetime.utcnow().isoformat() + "Z"
        }])