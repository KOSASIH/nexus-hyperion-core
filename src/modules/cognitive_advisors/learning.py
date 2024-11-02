# src/modules/cognitive_advisors/learning.py

import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Configure logging for the learning module
logger = logging.getLogger(__name__)

class FinancialPredictor:
    """Class to handle financial predictions using machine learning models."""

    def __init__(self):
        """Initialize the FinancialPredictor."""
        self.model = RandomForestRegressor()
        logger.info("FinancialPredictor initialized.")

    def train_model(self, data, target_column):
        """
        Train the financial prediction model.

        Args:
            data (pd.DataFrame): DataFrame containing features and target.
            target_column (str): The name of the target column to predict.
        """
        logger.info("Training financial prediction model.")
        X = data.drop(columns=[target_column])
        y = data[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        logger.info(f"Model trained with Mean Squared Error: {mse}")

    def predict(self, input_data):
        """
        Make predictions using the trained model.

        Args:
            input_data (pd.DataFrame): DataFrame containing input features.

        Returns:
            np.ndarray: Predicted values.
        """
        logger.info("Making predictions.")
        predictions = self.model.predict(input_data)
        return predictions

    def save_model(self, filename):
        """
        Save the trained model to a file.

        Args:
            filename (str): The filename to save the model.
        """
        import joblib
        joblib.dump(self.model, filename)
        logger.info(f"Model saved to {filename}.")

    def load_model(self, filename):
        """
        Load a trained model from a file.

        Args:
            filename (str): The filename to load the model from.
        """
        import joblib
        self.model = joblib.load(filename)
        logger.info(f"Model loaded from {filename}.")
