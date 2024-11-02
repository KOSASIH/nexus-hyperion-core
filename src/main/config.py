# src/main/config.py

import os
import json
import yaml

class Config:
    """Configuration settings for Nexus Hyperion."""

    def __init__(self, config_file=None):
        """Initialize configuration settings."""
        self.API_KEY = None
        self.DB_URI = None
        self.LOG_LEVEL = "INFO"
        self.load_environment_variables()
        if config_file:
            self.load_from_file(config_file)

    def load_environment_variables(self):
        """Load configuration from environment variables."""
        self.API_KEY = os.getenv("NEXUS_HYPERION_API_KEY", "your_api_key_here")
        self.DB_URI = os.getenv("DATABASE_URI", "sqlite:///nexus_hyperion.db")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

    def load_from_file(self, config_file):
        """Load configuration from a JSON or YAML file."""
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

        with open(config_file, 'r') as file:
            if config_file.endswith('.json'):
                self.load_json(file)
            elif config_file.endswith('.yaml') or config_file.endswith('.yml'):
                self.load_yaml(file)
            else:
                raise ValueError("Unsupported configuration file format. Use JSON or YAML.")

    def load_json(self, file):
        """Load configuration from a JSON file."""
        try:
            config_data = json.load(file)
            self.API_KEY = config_data.get("API_KEY", self.API_KEY)
            self.DB_URI = config_data.get("DB_URI", self.DB_URI)
            self.LOG_LEVEL = config_data.get("LOG_LEVEL", self.LOG_LEVEL).upper()
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON configuration: {e}")

    def load_yaml(self, file):
        """Load configuration from a YAML file."""
        try:
            config_data = yaml.safe_load(file)
            self.API_KEY = config_data.get("API_KEY", self.API_KEY)
            self.DB_URI = config_data.get("DB_URI", self.DB_URI)
            self.LOG_LEVEL = config_data.get("LOG_LEVEL", self.LOG_LEVEL).upper()
        except yaml.YAMLError as e:
            raise ValueError(f"Error decoding YAML configuration: {e}")

    def validate(self):
        """Validate required configuration settings."""
        if not self.API_KEY or not self.DB_URI:
            raise ValueError("API_KEY and DB_URI must be set in the configuration.")

    def __repr__(self):
        return f"<Config(API_KEY={self.API_KEY}, DB_URI={self.DB_URI}, LOG_LEVEL={self.LOG_LEVEL})>"
