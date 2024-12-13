#!/usr/bin/env python
import pandas as pd

FILE_PATH = '../data/clean/raw_analyst_ratings.csv'

# this will run when the module is imported
df = pd.read_csv(FILE_PATH)

PUBLICATION_GROUPED_BY_YEAR = df.groupby(['year']).size().reset_index()
PUBLICATION_GROUPED_BY_YEAR.columns = ["year", "count"]

PUBLICATION_GROUPED_BY_MONTH = df.groupby(['year', 'month']).size().reset_index()
PUBLICATION_GROUPED_BY_MONTH.columns = ["year", "month", "count"]

PUBLICATION_GROUPED_BY_DAY = df.groupby(['year', 'month', 'day']).size().reset_index()
PUBLICATION_GROUPED_BY_DAY.columns = ["year", "month", "day", "count"]

def count_publication_by_year(year: int):
    """
    Count the number of publications for a specific year.

    :param year: The year for which to count publications.
    :type year: int
    :returns: A DataFrame containing the count of publications for the specified year.
    :rtype: pandas.DataFrame
    """
    return PUBLICATION_GROUPED_BY_YEAR[PUBLICATION_GROUPED_BY_YEAR["year"] == year]


def count_publication_by_month(year: int, month: int):
    """
    Count the number of publications for a specific month in a specific year.

    :param year: The year for which to count publications.
    :type year: int
    :param month: The month for which to count publications (1-12).
    :type month: int
    :returns: A DataFrame containing the count of publications for the specified year and month.
    :rtype: pandas.DataFrame
    """
    return PUBLICATION_GROUPED_BY_MONTH[
        (PUBLICATION_GROUPED_BY_MONTH["year"] == year) &
        (PUBLICATION_GROUPED_BY_MONTH["month"] == month)
        ]


def count_publication_by_day(day: int, month: int, year: int):
    """
    Count the number of publications for a specific day, month, and year.

    :param day: The day for which to count publications (1-31).
    :type day: int
    :param month: The month for which to count publications (1-12).
    :type month: int
    :param year: The year for which to count publications.
    :type year: int
    :returns: A DataFrame containing the count of publications for the specified day, month, and year.
    :rtype: pandas.DataFrame
    """
    return PUBLICATION_GROUPED_BY_DAY[
        (PUBLICATION_GROUPED_BY_DAY["year"] == year) &
        (PUBLICATION_GROUPED_BY_DAY["month"] == month) &
        (PUBLICATION_GROUPED_BY_DAY["day"] == day)
        ]
