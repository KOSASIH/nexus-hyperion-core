# src/utils/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import logging

# Configure logging for the visualization module
logger = logging.getLogger(__name__)

class VisualizationTools:
    """Class for creating various visualizations."""

    @staticmethod
    def plot_line_chart(x, y, title='Line Chart', xlabel='X-axis', ylabel='Y-axis'):
        """
        Plot a line chart.

        Args:
            x (list or np.ndarray): X-axis data
            y (list or np.ndarray): Y-axis data.
            title (str): Title of the chart.
            xlabel (str): Label for the X-axis.
            ylabel (str): Label for the Y-axis.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, marker='o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()
        logger.info("Displayed line chart.")

    @staticmethod
    def plot_bar_chart(categories, values, title='Bar Chart', xlabel='Categories', ylabel='Values'):
        """
        Plot a bar chart.

        Args:
            categories (list): List of categories for the X-axis.
            values (list or np.ndarray): Values for each category.
            title (str): Title of the chart.
            xlabel (str): Label for the X-axis.
            ylabel (str): Label for the Y-axis.
        """
        plt.figure(figsize=(10, 6))
        sns.barplot(x=categories, y=values)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.show()
        logger.info("Displayed bar chart.")

    @staticmethod
    def plot_histogram(data, bins=10, title='Histogram', xlabel='Values', ylabel='Frequency'):
        """
        Plot a histogram.

        Args:
            data (list or np.ndarray): Data to plot.
            bins (int): Number of bins for the histogram.
            title (str): Title of the histogram.
            xlabel (str): Label for the X-axis.
            ylabel (str): Label for the Y-axis.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=bins, edgecolor='black')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid(axis='y')
        plt.show()
        logger.info("Displayed histogram.")

    @staticmethod
    def plot_scatter_plot(x, y, title='Scatter Plot', xlabel='X-axis', ylabel='Y-axis'):
        """
        Plot a scatter plot.

        Args:
            x (list or np.ndarray): X-axis data.
            y (list or np.ndarray): Y-axis data.
            title (str): Title of the scatter plot.
            xlabel (str): Label for the X-axis.
            ylabel (str): Label for the Y-axis.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, alpha=0.7)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()
        logger.info("Displayed scatter plot.")
