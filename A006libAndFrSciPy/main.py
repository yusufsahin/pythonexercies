# scipy_example.py
from scipy import linalg
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x = linalg.solve(a, b)
print("Solution of linear equations:", x)
