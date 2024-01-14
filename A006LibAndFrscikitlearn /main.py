# scikit_learn_example.py
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.dot(X, np.array([2])) + 3
model = LinearRegression().fit(X, y)
print("Predictions:", model.predict(X))
