#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 04:16:03 2023

@author: rafael
"""
###############         THIS VERSION IS THE STANDARD ONE WITH THE TIME EXACTLY AS REQUIRED IN THE MILESTONE DESCRIPTION      ##########################


import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import random

class Note:
    def __init__(self, frq, note):
        self._frq = frq
        self._note = note

    def get_frq(self):
        return self._frq

    def set_frq(self, frq):
        self._frq = frq

    def get_note(self):
        return self._note

    def set_note(self, note):
        self._note = note



#lists containg the right and left notes to be used.

"""
0 --> off
C --> 1 
D --> 2
E --> 3
F --> 4
G --> 5
A --> 6
B --> 7
"""
O3 = [Note(0,"off"),Note(130.81,"C3"),Note(146.83,"D3"),Note(164.81,"E3"),Note(174.61,"F"),Note(196,"G3"),Note(220 ,"A3"),Note(246.93,"B3")]
O4 =[Note(0,"off"),Note(261.63,"C4"),Note(293.66,"D4"),Note(329.63,"E4"),Note(349.23,"F4"),Note(392,"G4"),Note(440,"A4"),Note(493.88,"B4")]


print("Hello there! select which song do you wanna hear from the play list.\nchoose one of the following:\n1)to play only on th 4rd octive.\n2)to play on both.")
song = eval(input())



# only by 4th Octive
song1 = [0,1  ,0,1,  0,4,  0,4,  0,4,  0,4,  0,4,  0,3,  0,4,  0,5]

# both 3rd and 4th together.
song2 = [1,1,  1,1,  4,4,  4,4,  4,4,  4,4,  4,4,  3,3,  4,4,  5,5]

# playlist 
playlist =  [song1,song2]


N = int(len(song1)/2)
noteTime =0.23
delay =0.29


#the total time of playing music.
time = 3
t = np.linspace(0 , time ,12* 1024)

print("The number of pairs of notes is set to be:" ,N)

#initializes x to be a list filled with zeros.
x = np.zeros(12*1024)

#summing the played songs.
temp = 0

 
for j in range(0,N,1):
    ti = j  * delay
    Ti = noteTime
   
  
    FL = O3[playlist[song -1][2*j]].get_frq()
    FR = O4[playlist[song -1][2*j+1]].get_frq() 
    x = x + np.multiply( np.sin(2*np.pi * FL *t) + np.sin(2*np.pi* FR * t),np.where(np.logical_and( t >= ti , t <= ti + Ti)  ,1,0 ) )
    
plt.plot(t,x)
sd.play(x,3*1024)
