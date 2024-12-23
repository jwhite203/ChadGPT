import numpy as np

# Simple dataset: x (input) and y (output)
x = np.array([1, 2, 3, 4, 5])  # Input values
y = np.array([2, 4, 6, 8, 10])  # Output values (y = 2x)

# Initialize weights (slope) and bias
m = 0  # slope
b = 0  # bias
learning_rate = 0.01
epochs = 1000

# Gradient Descent to train the model
for _ in range(epochs):
    # Predicted values
    y_pred = m * x + b
    
    # Calculate gradients
    dm = -2 * np.sum(x * (y - y_pred)) / len(x)  # Derivative w.r.t. slope
    db = -2 * np.sum(y - y_pred) / len(x)       # Derivative w.r.t. bias
    
    # Update weights
    m -= learning_rate * dm
    b -= learning_rate * db

# Output the trained model parameters
print(f"Trained Model: y = {m:.2f}x + {b:.2f}")

# Test the model
test_x = 7
predicted_y = m * test_x + b
print(f"Prediction for x={test_x}: y={predicted_y:.2f}")
