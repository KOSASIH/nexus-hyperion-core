# src/modules/risk_assessment/risk_evaluator.py

import logging
from .risk_model import SimpleRiskModel, AdvancedRiskModel

# Configure logging for the risk evaluator module
logger = logging.getLogger(__name__)

class RiskEvaluator:
    """Class for evaluating risk using different risk models."""
    
    def __init__(self, config=None):
        """Initialize the RiskEvaluator with a configuration."""
        self.config = config or {}
        self.models = {
            "simple": SimpleRiskModel(),
            "advanced": AdvancedRiskModel(weights={"factor1": 0.5, "factor2": 1.5, "factor3": 2.0}),
        }
        logger.info("RiskEvaluator initialized with models: simple, advanced.")

    def register_model(self, model_name, model_instance):
        """Register a new risk model."""
        if model_name in self.models:
            logger.warning(f"Model '{model_name}' is already registered. Overwriting.")
        self.models[model_name] = model_instance
        logger.info(f"Model '{model_name}' registered successfully.")

    def evaluate_risk(self, entity_id, model_name, data):
        """Evaluate risk for a given entity using the specified model."""
        logger.info(f"Evaluating risk for entity '{entity_id}' using model '{model_name}'.")
        model = self.get_model(model_name)
        risk = model.calculate_risk(data)
        logger.info(f"Risk for entity '{entity_id}': {risk}")
        return risk

    def evaluate_risks_batch(self, entities, model_name):
        """Evaluate risks for a batch of entities using the specified model."""
        logger.info(f"Evaluating risks for batch of entities using model '{model_name}'.")
        results = {}
        for entity_id, data in entities.items():
            try:
                risk = self.evaluate_risk(entity_id, model_name, data)
                results[entity_id] = risk
            except Exception as e:
                logger.error(f"Error evaluating risk for entity '{entity_id}': {e}")
                results[entity_id] = None  # Store None or some error indicator
        return results

    def get_model(self, model_name):
        """Retrieve a registered risk model by name."""
        model = self.models.get(model_name)
        if model is None:
            logger.error(f"Model '{model_name}' not found.")
            raise ValueError(f"Model '{model_name}' not found.")
        logger.info(f"Retrieved model '{model_name}'.")
        return model
