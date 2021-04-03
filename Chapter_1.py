# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:52:47 2021

@author: Andrija
"""

#to do 1

loren = []
loren.append("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum hendrerit massa quis pulvinar. Etiam facilisis est nec varius mattis. Proin a dapibus metus. Suspendisse nunc justo, imperdiet a erat non, molestie interdum dolor. Nunc et neque et sem luctus pulvinar. Nam pretium ultrices mattis. In dignissim ligula tortor. Donec in urna sagittis, interdum tellus sit amet, vestibulum nunc. Curabitur a turpis in urna tempus fringilla ut ac leo.Donec porttitor ipsum arcu, tincidunt venenatis nibh gravida et. Nam iaculis pellentesque ullamcorper. Aliquam erat volutpat. Quisque massa tellus, mollis sed lacus ac, sollicitudin ornare lectus. Vestibulum non viverra arcu, ac fringilla magna. Vestibulum ultrices mattis lectus at consectetur. Aliquam eget velit nunc. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Mauris sit amet viverra sem. Integer convallis urna sapien, id imperdiet enim rutrum id. Phasellus lobortis lacus vitae sodales posuere. Sed eu felis id augue bibendum elementum sit amet ut ligula. Aenean lorem nibh, gravida vitae porttitor ut, semper eu sem. Aliquam id aliquet odio. Sed ut orci volutpat massa ultrices ornare.Nunc tincidunt nunc sed sem venenatis, vel sagittis metus sagittis. Aenean condimentum, dui hendrerit pharetra dictum, tortor ipsum molestie augue, sit amet fermentum arcu diam placerat dolor. Fusce urna lorem, dignissim ut risus at, vehicula malesuada urna. Phasellus luctus iaculis risus at porttitor. Fusce auctor erat et elit rutrum, nec fermentum arcu congue. Suspendisse nunc metus, luctus viverra ante at, pellentesque ullamcorper quam. Mauris est tellus, tempus semper auctor eleifend, varius quis enim. Maecenas nec tincidunt lectus. Donec et pulvinar sapien. Quisque at tincidunt mauris. Nullam sed mi lorem. In ultrices felis diam, quis dictum est dapibus at. In et velit lobortis, gravida risus vitae, efficitur purus.")


f = open ('C:/Users/Andrija/Desktop/Skola/Text.txt', 'a+')

for i in loren :
    f.write(str(i))

mylines = []                              # Declare an empty list
with open ('C:/Users/Andrija/Desktop/Skola/loren.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
    for line in myfile:                   # For each line of text,
        mylines.append(line)              # add that line to the list.
    for element in mylines:               # For each element in the list,
        print(element)                    # print it.
        
from lorem_text import lorem

for i in range(4):
    with open ('C:/Users/Andrija/Desktop/Skola/Text.txt', 'a+') as f:
        f.write(lorem.paragraphs(i))
        
#to do 2

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
                     
print(paper2)

#to do 3

import json

with open('data.json', 'w') as fp:
    json.dump(paper2, fp,  indent=4)
with open('data.json', 'r') as fp:
    test= json.load(fp)
    

# to do 4

import json 
import lxml.etree

xml_file = "C:/Users/Andrija/Desktop/Skola/data2.nxml"
root = lxml.etree.parse(xml_file)
root

date = root.xpath("//note/date/text()")
hour = root.xpath("//note/hour/text()")
to = root.xpath("//note/to/text()")
fromm = root.xpath("//note/from/text()")
body = root.xpath("//note/body/text()")

data = {"date" : date,
        "hour" : hour,
        "to" : to,
        "from" : fromm,
        "body" :body}
with open('data_nxml.json', 'w') as fp:
    json.dump(data, fp,  indent=4)
with open('data_nxml.json', 'r') as fp:
    result= json.load(fp)
result
