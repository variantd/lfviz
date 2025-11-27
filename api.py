from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow CORS for the Dash app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8050"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_loss_data():
    try:
        with open('data/loss_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": "Data file not found. Please run 'python tools/generate_data.py' to generate it."}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON data in data file."}

@app.get("/api/data")
def get_data():
    return load_loss_data()

