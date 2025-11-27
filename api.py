from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

app = FastAPI()

# Allow CORS for the Dash app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8050"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/data")
def get_data(amplitude: float = 1.0, frequency: float = 1.0):
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = amplitude * np.sin(frequency * np.sqrt(x**2 + y**2))
    return {"x": x.tolist(), "y": y.tolist(), "z": z.tolist()}
