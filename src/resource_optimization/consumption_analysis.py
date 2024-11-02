# src/modules/resource_optimization/consumption_analysis.py

import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging for the consumption analysis module
logger = logging.getLogger(__name__)

class ConsumptionAnalyzer:
    """Class to analyze resource consumption."""
    
    def __init__(self, settings=None):
        """
        Initialize the ConsumptionAnalyzer with optional settings.

        Args:
            settings (dict): Optional settings for the analyzer.
        """
        self.settings = settings or {}
        logger.info("ConsumptionAnalyzer initialized with settings: %s", self.settings)

    def analyze_consumption(self, data):
        """
        Analyze resource consumption data.

        Args:
            data (pd.DataFrame): DataFrame containing resource consumption data.

        Returns:
            dict: Analysis results including total consumption and averages.
        """
        logger.info("Starting consumption analysis.")
        try:
            total_consumption = data.sum()
            average_consumption = data.mean()
            consumption_summary = {
                "total_consumption": total_consumption.to_dict(),
                "average_consumption": average_consumption.to_dict(),
                "status": "success"
            }
            logger.info("Consumption analysis successful.")
            return consumption_summary
        except Exception as e:
            logger.error("Consumption analysis failed: %s", e)
            return {"error": str(e), "status": "failed"}

    def visualize_consumption(self, data, kind='bar'):
        """
        Visualize resource consumption data.

        Args:
            data (pd.DataFrame): DataFrame containing resource consumption data.
            kind (str): Type of plot to create (e.g., 'bar', 'line', 'heatmap').
        """
        logger.info("Visualizing consumption data with kind: %s", kind)
        try:
            plt.figure(figsize=(10, 6))
            if kind == 'bar':
                data.plot(kind='bar')
                plt.title('Resource Consumption (Bar Chart)')
            elif kind == 'line':
                data.plot(kind='line')
                plt.title('Resource Consumption (Line Chart)')
            elif kind == 'heatmap':
                sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
                plt.title('Resource Consumption Correlation Heatmap')
            else:
                logger.warning("Unsupported visualization kind: %s. Defaulting to bar chart.", kind)
                data.plot(kind='bar')
                plt.title('Resource Consumption (Bar Chart)')

            plt.xlabel('Resources')
            plt.ylabel('Consumption')
            plt.tight_layout()
            plt.show()
            logger.info("Consumption visualization successful.")
        except Exception as e:
            logger.error("Visualization failed: %s", e)

    def generate_report(self, data):
        """
        Generate a summary report of resource consumption.

        Args:
            data (pd.DataFrame): DataFrame containing resource consumption data.

        Returns:
            str: Summary report as a string.
        """
        logger.info("Generating consumption report.")
        try:
            analysis_results = self.analyze_consumption(data)
            report = "Resource Consumption Report\n"
            report += "=" * 30 + "\n"
            report += "Total Consumption:\n"
            for resource, total in analysis_results['total_consumption'].items():
                report += f"{resource}: {total}\n"
            report += "\nAverage Consumption:\n"
            for resource, average in analysis_results['average_consumption'].items():
                report += f"{resource}: {average}\n"
            logger.info("Report generation successful.")
            return report
        except Exception as e:
            logger.error("Report generation failed: %s", e)
            return f"Error generating report: {str(e)}"
