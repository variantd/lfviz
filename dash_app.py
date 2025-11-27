import dash
from dash import dcc, html
import plotly.graph_objects as go
import requests
import numpy as np

# Initialize the Dash app
app = dash.Dash(__name__)

def get_data_from_api():
    """Fetches data from the API."""
    api_url = "http://localhost:8000/api/data"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json(), None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching data from API: {e}"
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"

def create_3d_plot(data):
    """Creates the 3D landscape plot."""
    colorscale = [[0.0, 'blue'], [1.0, 'green']]
    fig = go.Figure(data=[go.Surface(z=data['z'], x=data['x'], y=data['y'], colorscale=colorscale, colorbar=dict(title='Loss Value'))])

    if 'training_path' in data and data['training_path']:
        path = np.array(data['training_path'])
        path_x, path_y, path_z = path[:, 0], path[:, 1], path[:, 2]
        fig.add_trace(go.Scatter3d(
            x=path_x, y=path_y, z=path_z,
            mode='lines+markers',
            line=dict(color='red', width=5),
            marker=dict(color='red', size=4),
            name='Training Path'
        ))

    fig.update_layout(
        title='3D Loss Landscape with Training Path',
        autosize=True,
        margin=dict(l=65, r=50, b=65, t=90)
    )
    return dcc.Graph(figure=fig)

def create_2d_plot(data):
    """Creates the 2D diagnostic plot."""
    if 'training_path' in data and data['training_path']:
        path = np.array(data['training_path'])
        loss_values = path[:, 2]
        steps = np.arange(len(loss_values))
        
        fig = go.Figure(data=go.Scatter(x=steps, y=loss_values, mode='lines+markers'))
        fig.update_layout(
            title='Loss vs. Training Steps',
            xaxis_title='Training Step',
            yaxis_title='Loss',
            autosize=True,
        )
        return dcc.Graph(figure=fig)
    return html.Div("No training path data to display.")

def create_metrics_display(data):
    """Creates the display for stability metrics."""
    std_dev = data.get('loss_std_dev')
    if std_dev is not None:
        return html.H3(f"Training Stability (Loss Std Dev): {std_dev:.4f}")
    return html.H3("Training Stability (Loss Std Dev): N/A")

# Fetch data and create layout
data, error_message = get_data_from_api()

if error_message:
    app.layout = html.Div(error_message)
else:
    app.layout = html.Div([
        html.H1("Loss Function Landscape Analysis"),
        html.Div([
            html.Div(create_3d_plot(data), style={'width': '60%', 'display': 'inline-block'}),
            html.Div([
                create_2d_plot(data),
                create_metrics_display(data)
            ], style={'width': '40%', 'display': 'inline-block', 'vertical-align': 'top'}),
        ])
    ])

if __name__ == '__main__':
    app.run(debug=True, port=8050)
