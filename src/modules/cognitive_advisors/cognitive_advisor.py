# src/modules/cognitive_advisors/cognitive_advisor.py

import logging
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Configure logging for the cognitive advisor module
logger = logging.getLogger(__name__)

class CognitiveFinancialAdvisor:
    """Class to provide cognitive financial advisory services."""

    def __init__(self):
        """Initialize the CognitiveFinancialAdvisor."""
        self.client_profiles = pd.DataFrame()
        self.model = LinearRegression()
        logger.info("CognitiveFinancialAdvisor initialized.")

    def add_client_profile(self, client_id, age, income, risk_tolerance, goals):
        """
        Add a new client profile.

        Args:
            client_id (str): Unique identifier for the client.
            age (int): Age of the client.
            income (float): Annual income of the client.
            risk_tolerance (str): Risk tolerance level (e.g., 'low', 'medium', 'high').
            goals (list): List of financial goals for the client.
        """
        new_profile = {
            'client_id': client_id,
            'age': age,
            'income': income,
            'risk_tolerance': risk_tolerance,
            'goals': goals
        }
        self.client_profiles = self.client_profiles.append(new_profile, ignore_index=True)
        logger.info(f"Added client profile: {new_profile}")

    def recommend_investments(self, client_id):
        """
        Recommend investments based on client profile.

        Args:
            client_id (str): Unique identifier for the client.

        Returns:
            list: Recommended investment options.
        """
        profile = self.client_profiles[self.client_profiles['client_id'] == client_id]
        if profile.empty:
            logger.warning(f"No profile found for client_id: {client_id}")
            return []

        risk_tolerance = profile['risk_tolerance'].values[0]
        if risk_tolerance == 'low':
            recommendations = ['Bonds', 'Fixed Deposits']
        elif risk_tolerance == 'medium':
            recommendations = ['Balanced Funds', 'Index Funds']
        else:
            recommendations = ['Stocks', 'Cryptocurrency', 'ETFs']

        logger.info(f"Investment recommendations for client_id {client_id}: {recommendations}")
        return recommendations

    def track_goals(self, client_id, goal, progress):
        """
        Track progress towards financial goals.

        Args:
            client_id (str): Unique identifier for the client.
            goal (str): Financial goal to track.
            progress (float): Progress made towards the goal (percentage).
        """
        if goal not in self.client_profiles['goals'].values:
            logger.warning(f"Goal '{goal}' not found for client_id: {client_id}")
            return

        logger.info(f"Tracking progress for client_id {client_id} on goal '{goal}': {progress}%")

    def predict_future_income(self, client_id):
        """
        Predict future income based on historical data.

        Args:
            client_id (str): Unique identifier for the client.

        Returns:
            float: Predicted future income.
        """
        profile = self.client_profiles[self.client_profiles['client_id'] == client_id]
        if profile.empty:
            logger.warning(f"No profile found for client_id: {client_id}")
            return None

        # Example data for prediction (in a real scenario, this would be historical income data)
        X = np.array([[profile['age'].values[0], profile['income'].values[0]]])
        y = np.array([profile['income'].values[0] * 1.05])  # Assuming a 5% growth rate

        # Train a simple linear regression model
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        self.model.fit(X_train, y_train)
        predicted_income = self.model.predict(X_test)

        logger.info(f"Predicted future income for client_id {client_id}: {predicted_income[0]}")
        return predicted_income[0]

    def generate_report(self):
        """
        Generate a summary report of all client profiles.

        Returns:
            str: Summary report as a string.
        """
        report = "Cognitive Financial Advisor Client Profiles Report\n"
        report += "=" * 50 + "\n"
        for index, row in self.client_profiles.iterrows():
            report += f"Client ID: {row['client_id']}\n"
            report += f"  Age: {row['age']}\n"
            report += f"  Income: {row['income']}\n"
            report += f"  Risk Tolerance: {row['risk_tolerance']}\n"
            report += f"  Goals: {', '.join(row['goals'])}\n"
            report += "-" * 50 + "\n"
        
        logger.info("Generated client profiles report.")
        return report
