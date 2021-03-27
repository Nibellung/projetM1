# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:19 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
#maj 27/03/21
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class Uplift(object):
    
    random_forest_control = RandomForestClassifier(n_estimators=10, max_depth=7)
    random_forest_treatement = RandomForestClassifier(n_estimators=10, max_depth=7)
    # n_estimators : nombre d'arbre
    # profondeur max des arbre
    #tous les jeux de données sont des numpy arrays
    def __init__(self, dA_control, dA_treatment , lA_control,lA_treatment,):
        self.dA_control = dA_control # DataSet d'apprentissage de l'arbe de controle
        self.dA_treatment = dA_treatment #Dataset d'apprentissage de l'arbre de traitement
        self.lA_control = lA_control # Labels d'apprentissage de l'arbre de controle
        self.lA_treatment = lA_treatment # Labels d'apprentissage de l'arbre de traitement
        
    def fit(self):
        self.random_forest_control.fit(self.dA_control, self.lA_control)
        self.random_forest_treatement.fit(self.dA_treatment, self.lA_treatment)
    
    #dT np array
    def predict(self,dT):
        result_control = self.random_forest_control.predict(dT)
        result_treatment = self.random_forest_treatement.predict(dT)
        returnValue =[]
        for i in range(len(result_control)):
            if result_control[i]==1:
                returnValue.append(1)
            else :
                returnValue.append(result_treatment)
        return returnValue
    
    def score(self,X,y):
        return np.sum(y == self.predict(X)) / len(X)