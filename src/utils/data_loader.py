# src/utils/data_loader.py

import pandas as pd
import logging

# Configure logging for the data loader module
logger = logging.getLogger(__name__)

class DataLoader:
    """Class for loading data from various sources."""

    @staticmethod
    def load_csv(file_path):
        """
        Load data from a CSV file.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            pd.DataFrame: Loaded data as a DataFrame.
        """
        try:
            data = pd.read_csv(file_path)
            logger.info(f"Loaded data from {file_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {file_path}: {e}")
            raise

    @staticmethod
    def load_excel(file_path, sheet_name=0):
        """
        Load data from an Excel file.

        Args:
            file_path (str): Path to the Excel file.
            sheet_name (str or int): Name or index of the sheet to load.

        Returns:
            pd.DataFrame: Loaded data as a DataFrame.
        """
        try:
            data = pd.read_excel(file_path, sheet_name=sheet_name)
            logger.info(f"Loaded data from {file_path}, sheet: {sheet_name}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {file_path}: {e}")
            raise

    @staticmethod
    def load_json(file_path):
        """
        Load data from a JSON file.

        Args:
            file_path (str): Path to the JSON file.

        Returns:
            pd.DataFrame: Loaded data as a DataFrame.
        """
        try:
            data = pd.read_json(file_path)
            logger.info(f"Loaded data from {file_path}")
            return data
        except Exception as e:
            logger.error(f"Error loading data from {file_path}: {e}")
            raise
