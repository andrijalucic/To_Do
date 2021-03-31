# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 20:41:40 2021

@author: Andrija
"""

paper = {"authors" : ["Auteur1","Auteur2","Auteur3"],
         "title" : "This is paper 1",
         "affiliations" : ["University of Mannheim","University of Strasbourg"],
         "ref" : ["This is ref 1","This is ref 2","This is ref 3"]}
print(paper)

paper2 = {"paper1":{"authors" : ["Yann leCun","Yoshua Bengio","Geoffrey Hinton"],
         "title" : ["Deep Learning"],
         "affiliations" : ["Facebook AI Research, 770 Broadway, New York, New York 10003 USA",
                           "New York University, 715 Broadway, New York, New York 10003, USA.Department of Computer Science and Operations,Research Université de Montréal, Pavillon André-Aisenstadt, PO Box 6128 Centre-Ville STN Montréal, Quebec H3C 3J7, Canada",
                           "Google, 1600 Amphitheatre Parkway, Mountain View, California 94043, USA.Department of Computer Science, University of Toronto, 6 King’s College Road, Toronto, Ontario M5S 3G4, Canada."],
         },"paper2":{"authors" : ["Ian J. Goodfellow","Jean Pouget-Abadie","Mehdi Mirza","Bing Xu","David Warde-Farley","Sherjil Ozair","Aaron Courville","Yoshua Bengio"],
         "title" : ["Generative Adversarial Nets"],
         "affiliations" : ["Departement d’informatique et de recherche opérationnelle Université de Montréal,Montreal, QC H3C 3J7",
                           "Jean Pouget-Abadie is visiting Universite de Montr ´ eal from Ecole Polytechnique",
                           "Departement d’informatique et de recherche opérationnelle Université de Montréal,Montreal, QC H3C 3J7",
                           "Departement d’informatique et de recherche opérationnelle Université de Montréal,Montreal, QC H3C 3J7",
                           "Departement d’informatique et de recherche opérationnelle Université de Montréal,Montreal, QC H3C 3J7",
                           "Sherjil Ozair is visiting Universite de Montréal from Indian Institute of Technology Delhi",
                           "Departement d’informatique et de recherche opérationnelle Université de Montréal,Montreal, QC H3C 3J7",
                           "Yoshua Bengio is a CIFAR Senior Fellow"]}}
import json
print(paper2)
with open('data.json', 'w') as fp:
    json.dump(paper2, fp,  indent=4)
with open('data.json', 'r') as fp:
    test= json.load(fp)
    
