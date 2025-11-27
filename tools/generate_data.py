import numpy as np
import json
import os

def generate_loss_landscape(n_points=200, n_minima=15, n_maxima=15, noise_level=0.00625):
    """
    Generates a complex synthetic loss landscape with high extrema density and non-convexity.
    """
    x = np.linspace(-26, 26, n_points)
    y = np.linspace(-26, 26, n_points)
    xx, yy = np.meshgrid(x, y)

    # 1. Initialize with a flat surface
    zz = np.zeros_like(xx)

    # 2. Add random wave patterns for ripples
    np.random.seed(123) # for reproducibility of waves
    n_waves = 20
    for _ in range(n_waves):
        freq_x = np.random.uniform(0.1, 0.5)
        freq_y = np.random.uniform(0.1, 0.5)
        phase_x = np.random.uniform(0, 2 * np.pi)
        phase_y = np.random.uniform(0, 2 * np.pi)
        amplitude = np.random.uniform(0.5, 1.5)
        zz += np.sin(xx * freq_x + phase_x) * np.cos(yy * freq_y + phase_y) * amplitude

    # 3. Add multiple Gaussian-like minima
    np.random.seed(42) # for reproducibility of minima
    minima_x = np.random.uniform(-25, 25, n_minima)
    minima_y = np.random.uniform(-25, 25, n_minima)
    minima_depth = np.random.uniform(2, 8, n_minima)
    minima_width = np.random.uniform(0.5, 1.5, n_minima)

    for i in range(n_minima):
        zz -= minima_depth[i] * np.exp(
            -((xx - minima_x[i])**2 / (2 * minima_width[i]**2) +
              (yy - minima_y[i])**2 / (2 * minima_width[i]**2))
        )

    # 4. Add multiple Gaussian-like maxima
    np.random.seed(1337) # for reproducibility of maxima
    maxima_x = np.random.uniform(-25, 25, n_maxima)
    maxima_y = np.random.uniform(-25, 25, n_maxima)
    maxima_height = np.random.uniform(2, 8, n_maxima)
    maxima_width = np.random.uniform(0.5, 1.5, n_maxima)

    for i in range(n_maxima):
        zz += maxima_height[i] * np.exp(
            -((xx - maxima_x[i])**2 / (2 * maxima_width[i]**2) +
              (yy - maxima_y[i])**2 / (2 * maxima_width[i]**2))
        )

    # 5. Add some random noise for higher entropy
    zz += np.random.normal(0, noise_level, zz.shape)

    # 6. Perform gradient descent
    path = perform_gradient_descent(zz, xx, yy)

    return {"x": xx.tolist(), "y": yy.tolist(), "z": zz.tolist(), "path": path}

def perform_gradient_descent(zz, xx, yy, start_point_idx=(50, 150), n_steps=50, learning_rate=5.0):
    """
    Performs gradient descent on the given surface.
    """
    zz = np.array(zz)
    grad_y, grad_x = np.gradient(zz)

    path = []
    current_pos_idx = np.array(start_point_idx, dtype=float)

    for _ in range(n_steps):
        # Get current integer indices
        yi, xi = int(round(current_pos_idx[0])), int(round(current_pos_idx[1]))

        # Boundary check
        if not (0 <= yi < zz.shape[0] and 0 <= xi < zz.shape[1]):
            break

        # Get z value and gradient at current position
        z = zz[yi, xi]
        grad = np.array([grad_y[yi, xi], grad_x[yi, xi]]) # grad is (dy, dx)

        # Record path point (in plot coordinates)
        path.append([xx[yi, xi], yy[yi, xi], z])

        # Update position (indices)
        current_pos_idx -= learning_rate * np.array([grad[0], grad[1]])

    return path

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
