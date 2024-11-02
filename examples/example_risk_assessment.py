# examples/example_risk_assessment.py

from src.modules.risk_assessment import RiskAssessment  # Adjust the import based on your actual module structure

def main():
    # Create an instance of the RiskAssessment class
    risk_assessment = RiskAssessment()

    # Example data for risk assessment
    likelihood = 5  # Scale from 1 to 10
    impact = 10     # Scale from 1 to 10

    # Calculate risk score
    risk_score = risk_assessment.calculate_risk_score(likelihood, impact)
    print(f"Calculated Risk Score: {risk_score}")

    # Identify risks based on a list of risk levels
    risks = risk_assessment.identify_risks(['low', 'medium', 'high'])
    print(f"Identified Risks: {risks}")

if __name__ == "__main__":
    main()
