# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:16 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
import utils
import numpy as np
from uplift import Uplift

def main():
    data, labels = utils.load_dataset("./test/testV2.csv", False, np.int) # chargement du fichier
    print(data)
    print(labels)
    
    dA, dT = utils.setTrainDataSet(data, 70) # partage des donnees en deux dataSet
    lA, lT = utils.setTrainDataSet(labels, 70) # Idem pour les labels
    uplift = Uplift(dA, dT, lA, lT)
    uplift.fit()
    
if __name__ == "__main__":
    main()