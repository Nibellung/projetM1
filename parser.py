# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:50:01 2021

@author: Pierre RIGAL, Victor GUILLEN, Romain MEUNIER
"""
from bs4 import BeautifulSoup
import csv


articles = [None]
lecteurs = []
bid = []

###################################################################################################

with open("../Recommandation_Data/All Bids of Conference - Papers per sub.htm", "r" ) as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, features="lxml")

for tr in soup.find('thead').find_next_sibling().find_all('tr'):
    articles.append(tr.get_text(separator=" ").split(".  ", 1)[0])

f.close()

###################################################################################################

with open("../Recommandation_Data/All Bids of Conference - Papers per reviewer.htm", "r" ) as f:
    html_doc = f.read()
    
soup = BeautifulSoup(html_doc, features="lxml")
bid_lec = []

for tr in soup.find('thead').find_next_sibling().find_all('tr'):
    if tr.has_attr("style"):
        lecteurs.append(tr.get_text(separator=" "))
        if bid_lec != []:
            bid.append(bid_lec)
        bid_lec = []
    else:
        art = tr.find_next().get_text(separator=" ")
        b = tr.find_all_next()[3].get_text(separator=" ")
        if b == "yes":
            bid_lec.append((art, 1))
        elif b == "maybe":
            bid_lec.append((art, 2))
        else:
            bid_lec.append((art, 3))
bid.append(bid_lec)
            
f.close()

###################################################################################################

with open("monFichier.csv", "w", newline="") as f_write:
    writer = csv.writer(f_write)
    writer.writerow(articles)
    ilecteur = 0
    for l in lecteurs:
        line = [l]
        for a in articles[1:]:
            inBid = False
            for (art, b) in bid[ilecteur]:
                if a == art:
                    line.append(b)
                    inBid = True
            if not inBid:
                line.append("0")
        writer.writerow(line)
        ilecteur += 1
                    
        

f_write.close()