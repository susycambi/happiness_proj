import os
import pandas as pd 
from typing import List

def whdata_to_csv(whdata_excel_file_path):

    ''' Read the World Happiness data at the provided path and extract training data and testing data. 

    For each training and testing dataset the label vector y is the Life Ladder and the feature matrix X includes Log GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices, Generosity and Perceptions of corruption.

    The data are saved as the following CSV files which are also retunred by the function in the following order:
    X_train_path
    y_train_path
    X_test_path
    y_test_path

    Parameters
    ----------
    whdata_excel_file_path

    Returns
    ---------
    X_train_path
    y_train_path
    X_test_path
    y_test_path

    '''
    # extract parent directory
    data_dir = os.path.dirname(whdata_excel_file_path)
    # read data
    wh_all_df = pd.read_excel(whdata_excel_file_path)
    # keep only columns of interest
    label_col = ["Life Ladder"]
    feature_cols = ["Log GDP per capita", "Social support", "Healthy life expectancy at birth", 
    "Freedom to make life choices", "Generosity", "Perceptions of corruption"]
    cols_of_interest = ["year"] + label_col + feature_cols
    wh_withna_df = wh_all_df[cols_of_interest]
    # remove na
    wh_df = wh_withna_df.dropna()
    # create row conditions 
    rows_2006_to_2019 = (wh_df["year"] <= 2019)
    rows_2020 = (wh_df["year"] == 2020)
    # create training and testing dfs
    X_train_df = wh_df.loc[rows_2006_to_2019, feature_cols]
    y_train_df = wh_df.loc[rows_2006_to_2019, label_col]
    X_test_df = wh_df.loc[rows_2020, label_col]
    y_test_df = wh_df.loc[rows_2020, label_col]
    # assign each file full path to a variable
    X_train_path = os.path.join(data_dir, "X_train.csv")
    y_train_path = os.path.join(data_dir, "y_train.csv")
    X_test_path = os.path.join(data_dir, "X_test.csv")
    y_test_path = os.path.join(data_dir, "y_test.csv")
    # write data to CSV files
    X_train_df.to_csv(X_train_path, index = False)
    y_train_df.to_csv(y_train_path, index = False)
    X_test_df.to_csv(X_test_path, index = False)
    y_test_df.to_csv(y_test_path, index = False)

    return X_train_path, y_train_path, X_test_path, y_test_path

