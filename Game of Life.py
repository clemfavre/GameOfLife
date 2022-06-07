# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:26:07 2022

@author: clem
"""

from math import*
from colorama import Fore,Style
import time



# defdeparture
grid=[[0,0,1,0,0,1,0,0,0,0,0,0],[0,1,1,1,1,0,1,0,0,0,0,0],[0,1,0,0,1,1,0,1,0,1,1,0],[0,1,1,0,0,1,0,0,0,1,0,0],[0,1,0,0,1,0,1,0,0,1,1,0],[0,0,0,1,1,0,0,0,0,1,0,0],[0,0,0,0,1,0,1,0,1,0,1,0],[0,1,0,1,0,0,0,0,0,0,0,0],[0,0,1,1,1,0,1,1,0,1,0,0],[0,0,0,1,1,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0]]
newgrid=grid
lines=10 # without the last line that is full of dead cells and that doesn't change of state
columns=10 # without the first and the last columns that are full of dead cells and that don't change of state
# more visually
# 0,0,1,0,0,1,0,0,0,0,0,0
# 0,1,1,1,1,0,1,0,0,0,0,0
# 0,1,0,0,1,1,0,1,0,1,1,0
# 0,1,1,0,0,1,0,0,0,1,0,0
# 0,1,0,0,1,0,1,0,0,1,1,0
# 0,0,0,1,1,0,0,0,0,1,0,0
# 0,0,0,0,1,0,1,0,1,0,1,0
# 0,1,0,1,0,0,0,0,0,0,0,0
# 0,0,1,1,1,0,1,1,0,1,0,0
# 0,0,0,1,1,0,0,1,1,0,0,0
# 0,0,0,0,0,0,0,0,0,0,0,0



def nextstep():
    grid=newgrid
    for i in range(0,lines):
        for j in range(1,columns+1):
            cells=0
            if grid[i-1][j-1]==1:
                cells=cells+1
            if grid[i-1][j]==1:
                cells=cells+1
            if grid[i-1][j+1]==1:
                cells=cells+1
            if grid[i][j-1]==1:
                cells=cells+1
            if grid[i][j+1]==1:
                cells=cells+1
            if grid[i+1][j-1]==1:
                cells=cells+1
            if grid[i+1][j]==1:
                cells=cells+1
            if grid[i+1][j+1]==1:
                cells=cells+1
            if cells<2 or cells>3:
                newgrid[i][j]=0
            if cells==3:
                newgrid[i][j]=1
    return(newgrid)
#print(nextstep())


def pause(p):
    timelimit=p
    time.sleep(p)
#pause(3)


def display():
    for k in range(0,lines+1):
        print(grid[k])
    print("space")
#display()

def main():
    n=int(input("Number of steps :"))
    p=int(input("Timelimit :"))
    for k in range(0,n):
        display()
        nextstep()
        pause(p)
main()



