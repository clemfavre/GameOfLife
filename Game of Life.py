# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:26:07 2022

@author: clem
"""

from math import*
from colorama import Fore,Style
import time

# defdeparture
# 0,1,0,0,1,0,0,0,0,0
# 1,1,1,1,0,1,0,0,0,0
# 1,0,0,1,1,0,1,0,1,1
# 1,1,0,0,1,0,0,0,1,0
# 1,0,0,1,0,1,0,0,1,1
# 0,0,1,1,0,0,0,0,1,0
# 0,0,0,1,0,1,0,1,0,1
# 1,0,1,0,0,0,0,0,0,0
# 0,1,1,1,0,1,1,0,1,0
# 0,0,1,1,0,0,1,1,0,0
# 0,0,0,0,0,0,0,0,0,0,0

# defdeparture
L=[0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
Lafter=[0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0]

# L[-11]=L[100]=[0]


def nextstep():
    L=Lafter
    for k in range(0,99):
        cells=0
        if L[k-11]==1:
            cells=cells+1
        if L[k-10]==1:
            cells=cells+1
        if L[k-9]==1:
            cells=cells+1
        if L[k-1]==1:
            cells=cells+1
        if L[k+1]==1:
            cells=cells+1
        if L[k+9]==1:
            cells=cells+1
        if L[k+10]==1:
            cells=cells+1
        if L[k+11]==1:
            cells=cells+1
        if cells<2 or cells>3:
            Lafter[k]=0
        if cells==3:
            Lafter[k]=1
    return(Lafter)

#print(nextstep())


def pause(p):
    timelimit=p
    time.sleep(p)
#pause(3)


def display():
    L=Lafter #bizzare
    for k in range(0,10):
        i=10*k
        Lk=[]
        Lk=Lk+[L[i]]+[L[i+1]]+[L[i+2]]+[L[i+3]]+[L[i+4]]+[L[i+5]]+[L[i+6]]+[L[i+7]]+[L[i+8]]+[L[i+9]]
        if k==0:
            L0=Lk
        elif k==1:
            L1=Lk
        elif k==2:
            L2=Lk
        elif k==3:
            L3=Lk
        elif k==4:
            L4=Lk
        elif k==5:
            L5=Lk
        elif k==6:
            L6=Lk
        elif k==7:
            L7=Lk
        elif k==8:
            L8=Lk
        else:
            L9=Lk
    print(L0)
    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print(L5)
    print(L6)
    print(L7)
    print(L8)
    print(L9)
#display()

def main():
    n=int(input("Number of steps :"))
    p=int(input("Timelimit :"))
    for k in range(0,n):
        display()
        nextstep()
        pause(p)
main()











































