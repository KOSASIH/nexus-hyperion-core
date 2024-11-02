# src/modules/ethical_governance/compliance.py

import logging
import pandas as pd

# Configure logging for the compliance module
logger = logging.getLogger(__name__)

class ComplianceChecker:
    """Class to perform compliance checks against governance policies."""

    def __init__(self, governance_framework):
        """
        Initialize the ComplianceChecker with a governance framework.

        Args:
            governance_framework (GovernanceFramework): An instance of GovernanceFramework.
        """
        self.governance_framework = governance_framework
        self.compliance_records = pd.DataFrame(columns=['record_id', 'policy_id', 'compliance_status'])
        logger.info("ComplianceChecker initialized.")

    def check_compliance(self, record_id, policy_id, compliance_status):
        """
        Check compliance against a specific policy.

        Args:
            record_id (str): Unique identifier for the compliance record.
            policy_id (str): Unique identifier for the policy being checked.
            compliance_status (str): Compliance status (e.g., 'compliant', 'non-compliant').
        """
        if policy_id not in self.governance_framework.policies['policy_id'].values:
            logger.warning(f"Policy ID {policy_id} not found in governance framework.")
            return

        new_record = {
            'record_id': record_id,
            'policy_id': policy_id,
            'compliance_status': compliance_status
        }
        self.compliance_records = self.compliance_records.append(new_record, ignore_index=True)
        logger.info(f"Compliance checked: {new_record}")

    def generate_compliance_report(self):
        """
        Generate a report of compliance checks.

        Returns:
            str: Summary report of compliance checks.
        """
        report = "Compliance Check Report\n"
        report += "=" * 50 + "\n"
        for index, row in self.compliance_records.iterrows():
            report += f"Record ID: {row['record_id']}\n"
            report += f"  Policy ID: {row['policy_id']}\n"
            report += f"  Compliance Status: {row['compliance_status']}\n"
            report += "-" * 50 + "\n"
        
        logger.info("Generated compliance report.")
        return report

    def get_compliance_status(self, policy_id):
        """
        Get the compliance status for a specific policy.

        Args:
            policy_id (str): Unique identifier for the policy.

        Returns:
            str: Compliance status for the specified policy.
        """
        if policy_id not in self.governance_framework.policies['policy_id'].values:
            logger.warning(f"Policy ID {policy_id} not found in governance framework.")
            return "Policy not found."

        compliance_status = self.compliance_records[self.compliance_records['policy_id'] == policy_id]
        if compliance_status.empty:
            logger.info(f"No compliance records found for policy ID {policy_id}.")
            return "No compliance records found."

        latest_status = compliance_status.iloc[-1]['compliance_status']
        logger.info(f"Latest compliance status for policy ID {policy_id}: {latest_status}")
        return latest_status
