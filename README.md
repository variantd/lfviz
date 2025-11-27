## 📉 Loss Function Landscape Analyzer (Scalable PoC)

This project is a Proof-of-Concept (PoC) for a scalable, full-stack application designed to visualize and analyze synthetic loss function landscapes. It demonstrates a **decoupled architecture** necessary for future expansion into a robust utility capable of handling complex data generation and high user traffic.

-----

## 🚀 Architecture

The application uses a **three-tier architecture**, with the backend and frontend services running independently. This separation ensures scalability, allows for independent service updates, and enables the use of high-performance tools in each domain.

| Layer | Technology | Role | Details |
| :--- | :--- | :--- | :--- |
| **Frontend (UI)** | **Plotly Dash** | Renders the interactive 3D visualizations, handles user input (sliders), and acts as the client to the API. | Built on top of Flask and React, providing a Pythonic approach to robust web UIs. |
| **Backend (API)** | **FastAPI** | Serves as the high-performance data endpoint. It accepts parameters and returns the calculated data as JSON. | Utilizes Starlette for asynchronous request handling. |
| **Data/Compute** | **NumPy, Plotly** | Handles the generation of the large, multi-dimensional synthetic loss function data arrays. | The core Python scientific computing libraries. |

-----

## ✨ Features

  * **Interactive 3D Visualization:** Displays the loss landscape as a rotatable and zoomable 3D surface plot.
  * **Decoupled Architecture:** Clean separation of concerns between the API (data) and the UI (presentation) for scalability.
  * **Dynamic Parameter Control:** Allows users to adjust function parameters (e.g., **Amplitude**, **Frequency**) via frontend sliders to instantly reshape the loss landscape.

-----

## ⚙️ Local Development Environment Setup (Ubuntu Linux)

These instructions assume you have **Python 3** and **`git`** installed on your Ubuntu system.

### 1\. Project Structure

Ensure your files are structured as follows:

```
loss-landscape-poc/
├── api.py           # FastAPI Backend Service
├── dash_app.py      # Plotly Dash Frontend Service
└── README.md
```

### 2\. Environment & Dependency Installation

It is highly recommended to use a virtual environment to isolate the project dependencies.

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install all required dependencies
pip install fastapi uvicorn plotly dash numpy requests
```

### 3\. Run the Services

Because this is a decoupled architecture, you must start the backend API and the frontend application in **two separate terminal sessions** or use nohup.

#### A. Start the Backend (API)

The API will run on the default port **8000**.

```bash
# In Terminal 1 (ensure venv is active)
uvicorn api:app --reload --port 8000
```

> **Output Confirmation:** You should see a message indicating the Uvicorn server is running at `http://127.0.0.1:8000`.

#### B. Start the Frontend (Dash App)

The Dash app will run on the default port **8050** and will attempt to fetch data from the running API.

```bash
# In Terminal 2 (ensure venv is active)
python dash_app.py
```

> **Access the App:** Open your web browser and navigate to the Dash application at: **http://localhost:8050**

-----

### 4\. Deactivating the Environment

When you are finished working on the project, you can exit the virtual environment:

```bash
deactivate
```