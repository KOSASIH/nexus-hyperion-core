# src/modules/risk_assessment/__init__.py

import logging
from .risk_model import RiskModel, SimpleRiskModel, AdvancedRiskModel
from .risk_evaluator import RiskEvaluator

# Configure logging for the risk assessment module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a console handler for logging
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

class RiskAssessmentModule:
    """Main class for managing risk assessment models and evaluations."""

    def __init__(self):
        """Initialize the RiskAssessmentModule with default models."""
        self.models = {}
        self.register_model("simple", SimpleRiskModel())
        self.register_model("advanced", AdvancedRiskModel(weights={"factor1": 0.5, "factor2": 1.5, "factor3": 2.0}))
        logger.info("RiskAssessmentModule initialized with default models.")

    def register_model(self, model_name, model_instance):
        """Register a new risk model."""
        if not isinstance(model_instance, RiskModel):
            logger.error(f"Model instance must be a subclass of RiskModel.")
            raise ValueError("Model instance must be a subclass of RiskModel.")
        
        self.models[model_name] = model_instance
        logger.info(f"Model '{model_name}' registered successfully.")

    def get_model(self, model_name):
        """Retrieve a registered risk model by name."""
        model = self.models.get(model_name)
        if model is None:
            logger.error(f"Model '{model_name}' not found.")
            raise ValueError(f"Model '{model_name}' not found.")
        logger.info(f"Retrieved model '{model_name}'.")
        return model

    def evaluate_risk(self, entity_id, model_name, data):
        """Evaluate risk for a given entity using the specified model."""
        logger.info(f"Evaluating risk for entity '{entity_id}' using model '{model_name}'.")
        model = self.get_model(model_name)
        risk = model.calculate_risk(data)
        logger.info(f"Risk for entity '{entity_id}': {risk}")
        return risk

# Expose the main classes for external use
__all__ = ["RiskAssessmentModule", "RiskModel", "SimpleRiskModel", "AdvancedRiskModel", "RiskEvaluator"]
