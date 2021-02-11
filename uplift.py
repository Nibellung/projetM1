# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:19 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import make_moons, load_breast_cancer
from sklearn.model_selection import train_test_split

class Uplift(object):

    def __init__(self, dfA:pd.DataFrame(), dfT:pd.DataFrame()) -> None:
        self.dfA = dfA # Dataframe d'apprentissage
        self.dfT = dfT # Dataframe de test

        
    def test(self) -> None:
        print(self.dfA)
        print(self.dfT)