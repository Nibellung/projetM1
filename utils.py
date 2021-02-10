# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:20 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
import csv
import numpy as np
import pandas as pd

def load_dataset(pathname:str) -> pd.DataFrame():
    """Load a dataset in csv format.

    Each line of the csv file represents a data from our dataset and each
    column represents the parameters.

    Parameters
    ----------
    pathname : str
        The path of the csv file.

    Returns
    -------
    data : DataFrame
        All data in the database.
    """
    # check the file format through its extension
    if pathname[-4:] != '.csv':
        raise OSError("The dataset must be in csv format")
    # open the file in read mode
    with open(pathname, 'r') as csvfile:
        # create the reader object in order to parse the data file
        reader = csv.reader(csvfile, delimiter=',')
        # extract the data
        data = []
        for row in reader:
            data.append(row)
        # converts Python lists into NumPy matrices
        data = np.array(data, dtype=np.str)
        
        # converts NumPy matrices into pandas dataframe
        df = pd.DataFrame(data, columns=["recency","history_segment","history","mens","womens","zip_code","newbie","channel","segment","visit","conversion","spend"])
        
    # return data
    return df