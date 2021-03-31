# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:18:50 2021

@author: Andrija
"""

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