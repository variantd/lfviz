import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Loss Function Landscape"),
    html.Div([
        html.Label("Amplitude"),
        dcc.Slider(
            id='amplitude-slider',
            min=0.1,
            max=2.0,
            step=0.1,
            value=1.0,
            marks={i/10: str(i/10) for i in range(1, 21, 3)},
        ),
    ], style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        html.Label("Frequency"),
        dcc.Slider(
            id='frequency-slider',
            min=0.1,
            max=2.0,
            step=0.1,
            value=1.0,
            marks={i/10: str(i/10) for i in range(1, 21, 3)},
        ),
    ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
    dcc.Graph(id='loss-landscape-graph')
])

# Callback to update the graph
@app.callback(
    Output('loss-landscape-graph', 'figure'),
    [Input('amplitude-slider', 'value'),
     Input('frequency-slider', 'value')]
)
def update_figure(amplitude, frequency):
    # Fetch data from the API
    api_url = "http://localhost:8000/api/data"
    params = {"amplitude": amplitude, "frequency": frequency}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()

        # Create the 3D surface plot
        figure = go.Figure(data=[go.Surface(z=data['z'], x=data['x'], y=data['y'])])
        figure.update_layout(
            title='3D Loss Landscape',
            autosize=False,
            width=800,
            height=800,
            margin=dict(l=65, r=50, b=65, t=90)
        )
        return figure
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        # Return an empty figure on error
        return go.Figure().update_layout(title="Error: Could not connect to API")


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
