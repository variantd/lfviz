import numpy as np
import json
import os

def generate_loss_landscape(n_points=100):
    """
    Generates a synthetic loss landscape with multiple local minima.
    """
    x = np.linspace(-5, 5, n_points)
    y = np.linspace(-5, 5, n_points)
    xx, yy = np.meshgrid(x, y)

    # Define multiple Gaussian-like minima
    minima = [
        {'A': 1.5, 'x0': 2, 'y0': 2, 'sx': 1, 'sy': 1},
        {'A': 1.2, 'x0': -2, 'y0': -3, 'sx': 1.5, 'sy': 1.5},
        {'A': 1.0, 'x0': -3, 'y0': 2, 'sx': 1, 'sy': 1},
        {'A': 0.8, 'x0': 3, 'y0': -2, 'sx': 2, 'sy': 2},
    ]

    zz = np.zeros_like(xx)
    for m in minima:
        zz -= m['A'] * np.exp(-((xx - m['x0'])**2 / (2 * m['sx']**2) + (yy - m['y0'])**2 / (2 * m['sy']**2)))

    return {"x": xx.tolist(), "y": yy.tolist(), "z": zz.tolist()}

if __name__ == "__main__":
    # Ensure the script is run from the root directory
    if not os.path.exists('tools'):
        print("Please run this script from the root directory of the project.")
        exit(1)

    data = generate_loss_landscape()
    
    # Create data directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    with open('data/loss_data.json', 'w') as f:
        json.dump(data, f)
    
    print("Synthetic loss landscape data generated and saved to data/loss_data.json")
