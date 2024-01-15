"""
You can add your own functions here according to your decision tree implementation.
There is no restriction on following the below template, these fucntions are here to simply help you.
"""

import numpy as np
import pandas as pd
from pd.api.types import is_numeric_dtype

def check_ifreal(y: pd.Series) -> bool:
    # Function to check if the given series has real or discrete values
    is_real = is_numeric_dtype(y)

    return is_real


def entropy(Y: pd.Series) -> float:
    # Function to calculate the entropy
    # unique values in Y
    unique_values = Y.value_counts()
    # probability of each value in unique_values
    norm = unique_values/unique_values.sum()
    # entropy of Y
    return norm.apply(lambda x: -x * np.log2(x + 1e-6)).sum()


def gini_index(Y: pd.Series) -> float:
    """
    Function to calculate the gini index
    """

    pass


def information_gain(Y: pd.Series, attr: pd.Series) -> float:
    """
    Function to calculate the information gain
    """

    pass


def opt_split_attribute(X: pd.DataFrame, y: pd.Series, criterion, features: pd.Series):
    """
    Function to find the optimal attribute to split about.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    features: pd.Series is a list of all the attributes we have to split upon

    return: attribute to split upon
    """

    # According to wheather the features are real or discrete valued and the criterion, find the attribute from the features series with the maximum information gain (entropy or varinace based on the type of output) or minimum gini index (discrete output).

    pass


def split_data(X: pd.DataFrame, y: pd.Series, attribute, value):
    """
    Funtion to split the data according to an attribute.
    If needed you can split this function into 2, one for discrete and one for real valued features.
    You can also change the parameters of this function according to your implementation.

    attribute: attribute/feature to split upon
    value: value of that attribute to split upon

    return: splitted data(Input and output)
    """

    # Split the data based on a particular value of a particular attribute. You may use masking as a tool to split the data.

    pass
