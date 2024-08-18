# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:57:03 2024

@author: Student
"""
from random import randint
print("Chon 'bao', 'bua', 'keo': "); chon = input(); rdom = randint(0,2)
if rdom == 0:
    rdom = 'bao'
elif rdom == 1:
    rdom = 'bua'
else:
    rdom = 'keo'
print('Ban chon: '+chon); print('He thong chon: '+rdom); print('Ket qua: ')
if chon == rdom:
    print('Hoa')
elif chon == 'bao':
    if rdom == 'keo':
        print('He thong thang')
    else:
        print('Ban thang')
elif chon == "bua":
      if rdom == "keo":
        print('Ban thang')
      else:
        print('He thong thang')
elif chon == "keo":
    if rdom == "bao":
        print("Ban thang")
    else:
        print("He thong thang")
