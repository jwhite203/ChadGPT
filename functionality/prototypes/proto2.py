import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Sigmoid derivative
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR problem)
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])

# Initialize weights and biases
weights = np.random.rand(2, 1)
bias = np.random.rand(1)
learning_rate = 0.1

# Train the neural network
for _ in range(10000):
    # Forward pass
    input_layer = inputs
    weighted_sum = np.dot(input_layer, weights) + bias
    predictions = sigmoid(weighted_sum)
    
    # Calculate error
    error = outputs - predictions
    
    # Backpropagation
    adjustments = error * sigmoid_derivative(predictions)
    weights += np.dot(input_layer.T, adjustments) * learning_rate
    bias += np.sum(adjustments) * learning_rate

# Test the neural network
print("Trained Weights:", weights)
print("Trained Bias:", bias)
for test in inputs:
    result = sigmoid(np.dot(test, weights) + bias)
    print(f"Input: {test}, Predicted Output: {np.round(result)}")
