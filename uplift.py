# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:19 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
from sklearn.ensemble import RandomForestClassifier

class Uplift(object):

    rf = RandomForestClassifier(n_estimators=10, max_depth=7)
    # n_estimators : nombre d'arbre
    # profondeur max des arbre
    
    def __init__(self, dA, dT, lA, lT):
        self.dA = dA # DataSet d'apprentissage
        self.dT = dT # DataSet de test
        self.lA = lA # Labels d'apprentissage
        self.lT = lT # Labels de test
        
    def fit(self):
        self.rf.fit(self.dA, self.lA)
    
    def predict(self):
        return self.rf.predict(self.dT)