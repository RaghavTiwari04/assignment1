import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray

class RegressorPlotter:
    def __init__(self, default_weights: ndarray = None, X: ndarray = None, y: ndarray = None) -> None:
        """
        Initialize the RegressorPlotter.

        Parameters:
        - default_weights: Default weights for the linear regression model.
        - X: Feature matrix.
        - y: Target values.
        """
        self.weights = default_weights
        self.X = X
        self.y = y
        self.n = self._get_n()

        if not self._check_dimensions():
            raise ValueError("Dimensions do not meet the requirements. "
                             "Please check X, y, and weights.")

    def _get_n(self):
        """
        Get the number of features.

        Returns:
        - Number of features.
        """
        return self.X.shape[1]

    def _check_dimensions(self):
        """
        Check if the dimensions of X, y, and weights are compatible.

        Returns:
        - True if dimensions are compatible, False otherwise.
        """
        try:
            if (self.n == len(self.weights) - 1) and (self.X.shape[0] == len(self.y)):
                return True
        except:
            return False

    def _line(self, m, x, c):
        """
        Compute the equation of a line.

        Parameters:
        - m: Slope of the line.
        - x: Input values.
        - c: Intercept of the line.

        Returns:
        - Values of the line for the given inputs.
        """
        return np.dot(m, x) + c

    def plot_2D(self):
        """
        Plot 2D data and regression lines.

        If there is only one feature, a scatter plot with a regression line is displayed.
        For multiple features, subplots are created with scatter plots and regression lines.

        Raises:
        - ValueError: If the dimensions are incompatible or if there are more than two features for 3D plotting.
        """
        if self.n == 1:
            fig, axs = plt.subplots(1, 1, figsize=(8, 2))
            axs.scatter(self.X[:, 0], self.y, label='Data Points', color='black')
            axs.plot(self.X[:, 0], self._line(self.weights[1], self.X[:, 0], self.weights[0]),
                     label='Regression Line', color='red')
            axs.set_xlabel('Feature 1')
            axs.set_ylabel('Target')
        else:
            rows = (self.n + 1) // 2
            columns = 2
            fig, axs = plt.subplots(rows, columns, figsize=(8, 8))
            for i in range(self.n):
                row = i // columns
                col = i % columns
                axs[row, col].scatter(self.X[:, i], self.y, label=f'Data Points (Feature {i})', color='black')
                axs[row, col].plot(self.X[:, i], self._line(self.weights[i + 1], self.X[:, i], self.weights[0]),
                                   label=f'Regression Line (Feature {i})', color='red')
                axs[row, col].set_xlabel(f'Feature {i + 1}')
                axs[row, col].set_ylabel('Target')
                axs[row, col].legend()
            for i in range(self.n, rows * columns):
                row = i // columns
                col = i % columns
                axs[row, col].axis('off')
        plt.tight_layout()
        plt.show()

    def plot_3D(self):
        """
        Plot 3D data and regression surface.

        If there are exactly two features, a 3D scatter plot with a regression surface is displayed.

        Raises:
        - ValueError: If the dimensions are incompatible or if there are more than two features for 3D plotting.
        """
        print("1")
        if self.n == 2:
            plot = plt.figure()
            ax = plot.add_subplot(111, projection='3d')
            ax.scatter(self.X[:, 0], self.y, self.X[:, 1], c='black', marker='o', label='Data Points')
            xx, yy = np.meshgrid(self.X[:, 0], self.X[:, 1])
            zz = self.weights[0] + self.weights[1] * xx + self.weights[2] * yy
            ax.plot_surface(xx, yy, zz, alpha=0.5, color='red', label='Regression Surface')
            ax.set_xlabel('Feature 0')
            ax.set_ylabel('Target')
            ax.set_zlabel('Feature 1')
            ax.legend()
            plt.show()
        else:
            raise ValueError("Could not plot in 3D with more than 2 features. Check your matrix X.")
