#!/usr/bin/env python
import numpy as np
import pandas as pd
from typing import List
import matplotlib.pyplot as plt

def plot_line_chart(x: pd.Series, y: pd.Series) -> None:
    """
    Plot a line chart for the given datasets

    :param x: The x-axis values
    :param y: The y-axis values
    :return: Nothing
    """
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, marker='o', linestyle='-')

    y_min = min(y)
    y_max = max(y)
    y_ticks = np.linspace(y_min, y_max + 1, 10)

    plt.xticks(x)
    plt.yticks(y_ticks)

    plt.grid(True)
    plt.show()


def plot_bar_chart(categories: pd.Series, values: List[int] | pd.Series, color: str = 'skyblue') -> None:
    """
    Plots a bar chart using the provided categories and values.

    :param categories: A Pandas Series containing the categories for the x-axis of the bar chart.
    :type categories: pd.Series

    :param values: A list of integers or a Pandas Series containing the values for the y-axis of the bar chart.
                   The length of this parameter must match the length of `categories`.
    :type values: List[int] | pd.Series

    :param color: The color of the bars in the chart. Default is 'skyblue'.
    :type color: str

    :returns: None
        This function does not return any value. It displays the bar chart directly.
    """
    plt.figure(figsize=(12, 6))
    plt.bar(categories, values, color=color)

    plt.grid(True)
    plt.show()

