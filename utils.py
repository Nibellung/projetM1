# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:20 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
import csv
import numpy as np

def load_dataset(pathname:str, firstLine:bool = True, dtype = np.str):
    """Load a dataset in csv format.

    Each line of the csv file represents a data from our dataset and each
    column represents the parameters.

    Parameters
    ----------
    pathname : str
        The path of the csv file.
    firstLine : bool
        heading
    dtype
        type of data
    Returns
    -------
    data, labels : tuple
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
        labels = []
        for row in reader:
            if firstLine:
                firstLine = False
            else:
                data.append(row[:-1])
                labels.append(row[-1])
        # converts Python lists into NumPy matrices
        data = np.array(data, dtype)
        labels = np.array(labels, dtype=np.float)

    return data, labels

"""************************************************************************"""

def setTrainDataSet(d:np.array, sizeTrainDataSet:int):
    """
    Separation du dataset en un dataset d'apprentissage
    et un dataset de test
    
    Parameters
    ----------
    d : np.array
        Les donnees du csv
    sizeTrainDataSet : int
        taille en % du dataset d'apprentissage
        
    Returns
    -------
    trainDataSet, testDataSet : tuple
        dataset d'entrainement et de test
    """
    lenD = len(d)
    sizeTrainDataSet = int(lenD * (sizeTrainDataSet / 100))
    trainDataSet = d[0:sizeTrainDataSet]
    testDataSet = d[sizeTrainDataSet+1:lenD]
    return trainDataSet, testDataSet

"""************************************************************************"""

def formaterFichierTest(d:np.array):
    """
    Prend le fichier de test et remplace toutes les chaines par des int
    et sauvegarde les nouvelles donnees
    
    Parameters
    ----------
    d : np.array
        Les donnees du csv
    """
    newFile = []
    for row in d:
        r = []
        for col in range(len(row)):
            if col == 0:
                r.append(int(row[col]))
            elif col == 1:
                pass
            elif col == 2:
                r.append(int(float(row[col])))
            elif col == 3:
                r.append(int(row[col]))
            elif col == 4:
                r.append(int(row[col]))
            elif col == 5:
                if row[col] == "Suburban":
                    r.append(0)
                elif row[col] == "Rural":
                    r.append(1)
                elif row[col] == "Urban":
                    r.append(2)
                else:
                    r.append(3)
            elif col == 6:
                r.append(int(row[col]))
            elif col == 7:
                if row[col] == "Phone":
                    r.append(0)
                elif row[col] == "Web":
                    r.append(1)
                elif row[col] == "Multichannel":
                    r.append(2)
                else:
                    r.append(3)
            elif col == 8:
                if row[col] == "Womens E-Mail":
                    r.append(0)
                elif row[col] == "Mens E-Mail":
                    r.append(1)
                elif row[col] == "No E-Mail":
                    r.append(2)
                else:
                    r.append(3)
            elif col == 9:
                r.append(int(row[col]))
            elif col == 10:
                r.append(int(row[col]))
            else:
                r.append(int(float(row[col])))
        newFile.append(r)

    newFile = np.array(newFile, dtype=np.int32)
    np.savetxt('test/testV2.csv', newFile, fmt="%d", delimiter=",")
        