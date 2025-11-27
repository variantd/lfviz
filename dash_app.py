import dash
from dash import dcc, html
import plotly.graph_objects as go
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

def create_figure():
    # Fetch data from the API
    api_url = "http://localhost:8000/api/data"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        if "error" in data:
            return html.Div(f"Error from API: {data['error']}")

        # Create the 3D surface plot
        colorscale = [[0.0, 'purple'], [0.5, 'blue'], [1.0, 'green']]
        figure = go.Figure(data=[go.Surface(z=data['z'], x=data['x'], y=data['y'], colorscale=colorscale, colorbar=dict(title='Loss Value'))])
        figure.update_layout(
            title='Synthetic Loss Landscape with Multiple Minima',
            autosize=True,
            margin=dict(l=65, r=50, b=65, t=90)
        )
        return dcc.Graph(figure=figure)
    except requests.exceptions.RequestException as e:
        return html.Div(f"Error fetching data from API: {e}")
    except Exception as e:
        return html.Div(f"An unexpected error occurred: {e}")

# App layout
app.layout = html.Div([
    html.H1("Loss Function Landscape"),
    create_figure()
])


if __name__ == '__main__':
    app.run(debug=True, port=8050)
