import csv
import json
import pickle
from multiple_linear_regression import MultipleLinearRegression
import numpy as np
import flake8

class ModelSaver:
    def __init__(self, default_file_format='csv'):
        """
        Initialize the ModelSaver.

        Parameters:
        - default_file_format: Default file format for saving/loading parameters ('csv', 'json', or 'pickle').
        """
        self.file_format = default_file_format

    def save_parameters(self, model, filename):
        """
        Save the parameters of the given model to a file.

        Parameters:
        - model: The model whose parameters need to be saved.
        - filename: The name of the file to save the parameters.
        """
        if self.file_format == 'csv':
            self._save_csv(model, filename)
        elif self.file_format == 'json':
            self._save_json(model, filename)
        elif self.file_format == 'pickle':
            self._save_pickle(model, filename)
        else:
            raise ValueError("Unsupported file format")

        print(f"Parameters saved in {self.file_format} format. Values: {model.get_params()}")

    def load_parameters(self, model, filename):
        """
        Load parameters from a file to the given model.

        Parameters:
        - model: The model to which parameters need to be loaded.
        - filename: The name of the file from which to load parameters.

        Returns:
        - Loaded parameters.
        """
        if self.file_format == 'csv':
            loaded_params = self._load_csv(filename)
        elif self.file_format == 'json':
            loaded_params = self._load_json(filename)
        elif self.file_format == 'pickle':
            loaded_params = self._load_pickle(filename)
        else:
            raise ValueError("Unsupported file format")

        return loaded_params

    def _save_csv(self, model, filename):
        """
        Save parameters to a CSV file.

        Parameters:
        - model: The model whose parameters need to be saved.
        - filename: The name of the file to save the parameters.
        """
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(model.get_params())

    def _load_csv(self, filename):
        """
        Load parameters from a CSV file.

        Parameters:
        - filename: The name of the file from which to load parameters.

        Returns:
        - Loaded parameters.
        """
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                params = next(reader)
                parameters = [float(param) for param in params]
                return self._set_params(parameters)
        except FileNotFoundError:
            print(f"File not found: {filename}")

    def _save_json(self, model, filename):
        """
        Save parameters to a JSON file.

        Parameters:
        - model: The model whose parameters need to be saved.
        - filename: The name of the file to save the parameters.
        """
        with open(filename, 'w') as jsonfile:
            json.dump({'params': model.get_params()}, jsonfile)

    def _load_json(self, filename):
        """
        Load parameters from a JSON file.

        Parameters:
        - filename: The name of the file from which to load parameters.

        Returns:
        - Loaded parameters.
        """
        try:
            with open(filename, 'r') as jsonfile:
                data = json.load(jsonfile)
                return self._set_params(data['params'])
        except FileNotFoundError:
            print(f"File not found: {filename}")

    def _save_pickle(self, model, filename):
        """
        Save parameters to a pickle file.

        Parameters:
        - model: The model whose parameters need to be saved.
        - filename: The name of the file to save the parameters.
        """
        with open(filename, 'wb') as picklefile:
            pickle.dump(model.get_params(), picklefile)

    def _load_pickle(self, filename):
        """
        Load parameters from a pickle file.

        Parameters:
        - filename: The name of the file from which to load parameters.

        Returns:
        - Loaded parameters.
        """
        try:
            with open(filename, 'rb') as picklefile:
                return self._set_params(pickle.load(picklefile))
        except FileNotFoundError:
            print(f"File not found: {filename}")
            
    def _set_params(self, parameters):
        """
        Set parameters to a new model.

        Parameters:
        - parameters: List of parameters.

        Returns:
        - New model with the specified parameters.
        """
        weights = np.array(parameters)
        model = MultipleLinearRegression(default_weights=weights)
        return model
