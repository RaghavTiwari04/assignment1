from multiple_linear_regression import MultipleLinearRegression
from regression_plotter import RegressorPlotter
from model_saver import ModelSaver
from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd

def main():
    """
    m = ModelSaver(default_file_format ='pickle')
    x = np.array([1,2,3,4,5,6,7,8,9])
    model3 = MultipleLinearRegression(default_weights = x)
    file_name = "parameters.pickle"
    m.save_parameters(model3, file_name)
    model2 = m.load_parameters(model3, file_name)       
    print(model2.weights)

    
    diabetes_data = load_diabetes()
    X = diabetes_data.data
    y = diabetes_data.target
    model = MultipleLinearRegression()
    model.train(X, y)
    print(model.weights)
    x = np.array([1,2,3,4,5,6,7,8,9,101])
    print(model.predict(x))
    
    model1 = RegressorPlotter(model.weights, X, y)
    model1.plot_2D()
    
    Q = np.array([[2,3],
                 [3,4]])
    y = np.array([2,3])
    ws = np.array([3,4,5])
    model5 = RegressorPlotter(ws, Q, y)
    model5.plot_3D()
    """
    
if __name__ == "__main__":
    main()
    