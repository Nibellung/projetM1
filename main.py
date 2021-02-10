# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:15:16 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
from utils import load_dataset

def main():
    data = load_dataset("./test/test_data.csv")
    print(data)

if __name__ == "__main__":
    main()