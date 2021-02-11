# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:16 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
from utils import load_dataset, setTrainDataSet
from uplift import Uplift

def main():
    data = load_dataset("./test/test_data.csv") # chargement du fichier csv
    dfA, dfT = setTrainDataSet(data, 70) # partage des donnees en deux dataframes
    uplift = Uplift(dfA, dfT)
    uplift.test()
    
if __name__ == "__main__":
    main()