# 📉 Loss Function Landscape Analyzer

This project is a full-stack application designed to visualize and analyze complex, synthetic loss function landscapes. It demonstrates a decoupled architecture and provides tools for visual and quantitative analysis of a simulated model training process.

-----

## 🚀 Architecture

The application uses a **three-tier architecture** with decoupled data generation, a backend API, and a frontend UI.

| Layer | Technology | Role | Details |
| :--- | :--- | :--- | :--- |
| **Frontend (UI)** | **Plotly Dash** | Renders interactive 3D and 2D visualizations of the loss landscape and training metrics. | Acts as a client to the data API. |
| **Backend (API)** | **FastAPI** | Serves the pre-generated loss landscape and training run data as a high-performance JSON endpoint. | Utilizes Starlette for asynchronous request handling. |
| **Data Generation** | **NumPy** | A suite of scripts to generate a complex, high-entropy synthetic loss landscape and simulate a training run using gradient descent. | The generated data is stored in a JSON file, decoupling data generation from the live application. |

-----

## ✨ Features

*   **Complex Synthetic Data:** Generates a high-dimensional, non-convex loss landscape with high extrema density to simulate a realistic production scenario.
*   **Simulated Training Run:** Simulates a model training process using gradient descent and visualizes the optimization path.
*   **Dual-View Analysis:**
    *   **3D View:** An interactive 3D plot of the loss landscape with the training path overlaid.
    *   **2D View:** A diagnostic plot of the loss value over the training steps.
*   **Quantitative Stability Metrics:** Calculates and displays the standard deviation of the loss during the training run to provide insights into training stability.
*   **Decoupled Architecture:** Clean separation between the data generation, API, and UI for scalability and maintainability.

-----

## ⚙️ Local Development Environment Setup (Ubuntu Linux)

These instructions assume you have **Python 3** and **`git`** installed on your Ubuntu system.

### 1\. Project Structure

The project is structured as follows:

```
lfviz/
├── data/
│   └── loss_data.json   # (Git-ignored) Generated data file
├── tools/
│   ├── bootstrap.sh
│   └── generate_data.py # Script to generate the synthetic data
├── .gitignore
├── api.py               # FastAPI Backend Service
├── dash_app.py          # Plotly Dash Frontend Service
└── README.md
```

### 2\. Environment & Dependency Installation

It is highly recommended to use a virtual environment. The `tools/bootstrap.sh` script can be used to set up the environment and install dependencies.

```bash
# 1. Make the bootstrap script executable
chmod +x tools/bootstrap.sh

# 2. Run the bootstrap script
./tools/bootstrap.sh
```
Alternatively, you can set up the environment manually:
```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install all required dependencies
pip install fastapi uvicorn plotly dash numpy requests
```

### 3\. Run the Application

The application requires three steps to run: data generation, starting the backend API, and starting the frontend UI.

#### A. Generate the Data

First, run the data generation script to create the `loss_data.json` file.

```bash
# Ensure your virtual environment is active
source venv/bin/activate

# Run the script
python3 tools/generate_data.py
```

#### B. Start the Backend (API)

The API serves the generated data and runs on port **8000**.

```bash
# In Terminal 1 (ensure venv is active)
uvicorn api:app --reload --port 8000
```

> **Output Confirmation:** You should see a message indicating the Uvicorn server is running at `http://127.0.0.1:8000`.

#### C. Start the Frontend (Dash App)

The Dash app consumes the data from the API and runs on port **8050**.

```bash
# In Terminal 2 (ensure venv is active)
python3 dash_app.py
```

> **Access the App:** Open your web browser and navigate to the Dash application at: **http://localhost:8050**

-----

### 4\. Deactivating the Environment

When you are finished, you can exit the virtual environment:

```bash
deactivate
```
