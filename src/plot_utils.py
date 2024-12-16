#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Union, Any


def plot_line_chart(x: Union[pd.Series, List[Union[int, str]]], y: Union[pd.Series, List[int]], **kwargs: Any) -> None:
    """
    Plot a line chart for the given datasets

    :param x: The x-axis values
    :param y: The y-axis values
    :return: Nothing
    """
    plt.figure(figsize=kwargs.pop('figsize', (12, 6)))
    plt.title(kwargs.pop('title', ''))
    plt.plot(x, y, marker='o', linestyle='-')

    # y_min = min(y)
    # y_max = max(y)
    # y_ticks = np.linspace(y_min, y_max + 1, 10)

    plt.xticks(x)
    # plt.yticks(y_ticks)

    plt.grid(True)
    plt.show()


def plot_bar_chart(categories: List[str], values: List[int] | pd.Series, **kwargs: Any) -> None:
    """
    Plots a bar chart using the provided categories and values.

    :param categories: A Pandas Series containing the categories for the x-axis of the bar chart.
    :type categories: pd.Series

    :param values: A list of integers or a Pandas Series containing the values for the y-axis of the bar chart.
                   The length of this parameter must match the length of `categories`.
    :type values: List[int] | pd.Series

    :returns: None
        This function does not return any value. It displays the bar chart directly.
    """
    plt.figure(figsize=kwargs.pop('figsize', (12, 6)))
    plt.grid(kwargs.pop('grid', False))

    plt.bar(categories, values, **kwargs)

    plt.show()


def plot_pie_chart(sizes: Union[List[int], pd.Series], labels: List[str]) -> None:
    """
    Plots a pie chart using the provided sizes.

    :param labels: A list of strings used as labels for the pie chart values
    :type labels: List[str]
    :param sizes: A list of integers or a Pandas Series containing the sizes for the pie chart.
    :type sizes: List[int] | pd.Series

    :returns: None
        This function does not return any value. It displays the pie chart directly.
    """
    plt.figure(figsize=(12, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    plt.show()
