import numpy as np
import pandas as pd
from numpy.linalg import inv, LinAlgError
from numpy import ndarray

class MultipleLinearRegression:
 
    def __init__(self, default_weights=None):
        """
        Initialize the MultipleLinearRegression model.

        Parameters:
        - default_weights: Initial weights for the model. If None, an empty array is used.
        """
        if default_weights is None:
            self.weights = np.array([])
        else:
            self.weights = np.array(default_weights)
  
    def _check_dimensions(self, X, y):
        """
        Check if the dimensions of X and y are valid.

        Parameters:
        - X: Feature matrix.
        - y: Target values.

        Returns:
        - X, y: Validated feature matrix and target values.
        """
        try:
            # Check if the number of rows of X is the same as the number of elements in y
            if len(y) == X.shape[0]:
                return X, y
            else:
                raise ValueError("Number of rows in X does not match the length of y")
        except ValueError as e:
            print(f"Error: {e}")
    
    def train(self, X: ndarray, y: ndarray) -> None:
        """
        Train the MultipleLinearRegression model.

        Parameters:
        - X: Feature matrix.
        - y: Target values.
        """
        X, y = self._check_dimensions(X, y)
        rows = X.shape[0]
        ones = np.ones((rows))
        new_X = np.insert(X, 0, ones, axis=1)
        try:
            self.weights = np.dot(np.dot(inv(np.dot(new_X.T, new_X)), new_X.T), y)
        except LinAlgError as e:
            print(f"Error: {e}")
            raise ValueError("Matrix inversion failed. Check if the matrix is singular or not invertible.")
       
    def predict(self, x: ndarray) -> None:
        """
        Make predictions with the trained model.

        Parameters:
        - x: Feature matrix for prediction.

        Returns:
        - Predicted values.
        """
        while True:
            try:
                if len(self.weights) - 1 == len(x):
                    return np.dot(x, self.weights[1:]) + self.weights[0]
                else:
                    raise ValueError("The dimensions of X do not match with the number of weights.")
            except ValueError as e:
                print(f"Error: {e}")
                x_input = input("Please enter a new x matrix: ")
                x = np.array(eval(x_input))
        
    def get_params(self):
        """
        Get the parameters (weights) of the model.

        Returns:
        - List of model parameters.
        """
        weights = self.weights.tolist()
        return weights
