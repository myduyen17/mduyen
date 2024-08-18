# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:09:12 2024

@author: Student
"""
import math
a = float(input("Nhập quãng đường (km):"))
if a==1:
    b=20
    print("số tiền : ", b ,"k")    
elif a >= 1 and a <= 3 :
    b=a*13
    print("số tiền : ", b , "k")
elif a >= 4 and a <= 8 :
    b=a*12
    print("số tiền : ", b , "k")
elif a >= 9 and a <= 10 :
    b=a*10
    print("số tiền : ", b , "k")    
if a >= 100 :
    b=a*0.92
    print("số tiền : ", b)    
  