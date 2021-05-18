# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:19 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
#maj 27/03/21
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

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
    
"""
Entrée  : None
Sortie  : Récupère les lecteurs dans le fichier crée bid.csv et convertit le fichier en matrice numpy
"""

def recupererLecteurFromBid():
  data=pd.read_csv('./bid.csv')
  data=data.to_numpy()
  return data

"""
Entrée  : un entier numarticle
Sortie  : Récupère les labels de chaque reviewers pour un article numarticle
"""
def recupererLabelforAnArticle(numarticle):
  label=pd.read_csv('./score/score'+str(numarticle)+'.csv')
  label=label.to_numpy()
  return label

"""
Entrée  : les données récupérees grace a recupererLecteurFromBid
Sortie  : les données séparées entre les données de traitement et les données de controle,
 ainsi qu'une liste des identifiants liés séparés de la même facon
"""
def split_data(data):
  data_control = []
  id_control =[]
  data_treatment = []
  id_treatment = []
  for i in data:
    if i[1]==0: 
      data_treatment.append(i)
      id_treatment.append(i[0])
    else :
      data_control.append(i)
      id_control.append(i[0])
  data_control=sorted(data_control, key = lambda data : data[0])
  data_control=np.array(data_control)
  data_control=np.delete(data_control,0,1)
  data_control=np.delete(data_control,0,1)
  data_treatment=sorted(data_treatment, key = lambda data : data[0])
  data_treatment=np.array(data_treatment)
  data_treatment=np.delete(data_treatment,0,1)
  data_treatment=np.delete(data_treatment,0,1)
  id_control=np.array(id_control)
  id_treatment=np.array(id_treatment)
  return data_control,data_treatment, id_control,id_treatment

"""
Entrée  : les labels d'un article avec les reviwers associé, 
          la liste des identifiants des reviwers du jeu de controle
          et la liste des identifients des reviewers du jeu de traitement
Sortie  : liste label_contol et label_traitement qui correnspondent au label respectivement
          liés au jeu de controle et au jeu de traitement
Note    : La fonction s'assure que chaque label soit bien associé au bon revierwer
"""
def association_label(label,id_control,id_treatment):
  label_control=[]
  label_treatment=[]
  for i in label :
    if np.any(id_control == i[0]) :
      label_control.append(i)
    else:
      label_treatment.append(i)
  label_control=sorted(label_control, key = lambda label : label[0])
  label_control=np.array(label_control)
  label_control=np.delete(label_control,0,1)
  label_treatment=sorted(label_treatment, key = lambda label : label[0])
  label_treatment=np.array(label_treatment)
  label_treatment=np.delete(label_treatment,0,1)
  return label_control,label_treatment