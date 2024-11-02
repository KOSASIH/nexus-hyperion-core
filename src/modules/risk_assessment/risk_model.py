# src/modules/risk_assessment/risk_model.py

import numpy as np
import logging

# Configure logging for the risk model module
logger = logging.getLogger(__name__)

class RiskModel:
    """Base class for risk models."""
    
    def calculate_risk(self, data):
        """Calculate risk based on input data."""
        raise NotImplementedError("Subclasses should implement this method.")

    def validate_data(self, data):
        """Validate input data for risk calculation."""
        if not isinstance(data, dict):
            logger.error("Data must be a dictionary.")
            raise ValueError("Data must be a dictionary.")
        logger.debug("Data validation passed.")

class SimpleRiskModel(RiskModel):
    """A simple risk model based on a linear scoring system."""
    
    def calculate_risk(self, data):
        """Calculate risk using a simple linear model."""
        logger.debug("Calculating risk using SimpleRiskModel.")
        self.validate_data(data)
        
        score = sum(data.values())
        risk = score / len(data) if data else 0
        logger.info(f"Calculated risk: {risk}")
        return risk

class AdvancedRiskModel(RiskModel):
    """An advanced risk model using a weighted scoring system."""
    
    def __init__(self, weights):
        """Initialize with weights for each factor."""
        self.weights = weights
        logger.debug(f"AdvancedRiskModel initialized with weights: {weights}")

    def validate_data(self, data):
        """Validate input data for the advanced risk model."""
        super().validate_data(data)
        
        if len(data) != len(self.weights):
            logger.error("Data and weights must have the same length.")
            raise ValueError("Data and weights must have the same length.")
        logger.debug("Data validation passed for AdvancedRiskModel.")

    def calculate_risk(self, data):
        """Calculate risk using a weighted model."""
        logger.debug("Calculating risk using AdvancedRiskModel.")
        self.validate_data(data)
        
        weighted_scores = [data[key] * self.weights[key] for key in data]
        risk = sum(weighted_scores) / sum(self.weights.values())
        logger.info(f"Calculated risk: {risk}")
        return risk

class CustomRiskModel(RiskModel):
    """A custom risk model that allows for user-defined risk calculation logic."""
    
    def __init__(self, calculation_function):
        """Initialize with a custom calculation function."""
        self.calculation_function = calculation_function
        logger.debug("CustomRiskModel initialized with a custom calculation function.")

    def calculate_risk(self, data):
        """Calculate risk using the custom calculation function."""
        logger.debug("Calculating risk using CustomRiskModel.")
        self.validate_data(data)
        
        risk = self.calculation_function(data)
        logger.info(f"Calculated risk: {risk}")
        return risk
