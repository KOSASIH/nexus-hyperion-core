# src/utils/metrics.py

import numpy as np
import logging

# Configure logging for the metrics module
logger = logging.getLogger(__name__)

class PerformanceMetrics:
    """Class for calculating various performance metrics."""

    @staticmethod
    def mean_squared_error(y_true, y_pred):
        """
        Calculate Mean Squared Error (MSE).

        Args:
            y_true (np.ndarray): True values.
            y_pred (np.ndarray): Predicted values.

        Returns:
            float: Mean Squared Error.
        """
        mse = np.mean((y_true - y_pred) ** 2)
        logger.info(f"Calculated Mean Squared Error: {mse}")
        return mse

    @staticmethod
    def r_squared(y_true, y_pred):
        """
        Calculate R-squared (coefficient of determination).

        Args:
            y_true (np.ndarray): True values.
            y_pred (np.ndarray): Predicted values.

        Returns:
            float: R-squared value.
        """
        ss_res = np.sum((y_true - y_pred) ** 2)
        ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        logger.info(f"Calculated R-squared: {r2}")
        return r2

    @staticmethod
    def accuracy(y_true, y_pred):
        """
        Calculate accuracy.

        Args:
            y_true (np.ndarray): True values.
            y_pred (np.ndarray): Predicted values.

        Returns:
            float: Accuracy as a percentage.
        """
        correct_predictions = np.sum(y_true == y_pred)
        accuracy = correct_predictions / len(y_true)
        logger.info(f"Calculated Accuracy: {accuracy * 100:.2f}%")
        return accuracy
