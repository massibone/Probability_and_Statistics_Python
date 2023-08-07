import math
import os
import re, sys, random

def standardDev(arr):
    mean=sum(arr)/len(arr)
    square=[(x-mean)**2 for x in arr]
    sum_square=sum(square)/len(arr)
    result=float(math.sqrt(sum_square))
    print(round(result,1))

if __name__ == '__main__':
    n=int(input().strip())
    val=list(map(int, input().rstrip().split()))
    standardDev(val)

'''
dati inseriti
5  (premi invio)
10 40 30 50 20   (inserire 5 valori dare uno spazio e dopo il 20 premi invio )
'''
#RISULTATO 14.1