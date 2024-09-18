import pandas as pd
from scripts.utils.custom_exceptions import CustomException
import sys

def check_outliers(data, features):
    """
    Check for outliers in the given dataset features using IQR method.
    
    Args:
        data (DataFrame): The DataFrame containing the data to check for outliers.
        features (list): A list of feature names to check for outliers.

    Returns:
        tuple: A tuple containing:
            - outlier_indexes (dict): A dictionary mapping feature names to lists of outlier indexes.
            - outlier_counts (dict): A dictionary mapping feature names to the count of outliers.
            - total_outliers (int): The total count of outliers in the dataset.
    """
    try:
        outlier_indexes = {}
        outlier_counts = {}
        total_outliers = 0
        
        for feature in features:
            Q1 = data[feature].quantile(0.25)
            Q3 = data[feature].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Identificar os outliers
            outliers = data[(data[feature] < lower_bound) | (data[feature] > upper_bound)]
            outlier_indexes[feature] = outliers.index.tolist()
            
            # Contar a quantidade de outliers
            outlier_count = len(outliers)
            outlier_counts[feature] = outlier_count
            total_outliers += outlier_count
        
        return outlier_indexes, outlier_counts, total_outliers

    except Exception as e:
        raise CustomException(e, sys)
