# SN = Sum(1-N) Xn    1 <= n <= N    Xn independent
# Xn = 1 v Xn = -1  with P(Xn) = 0.5 ;  N = 0 -> SN = 0 

import random
import numpy as np
import matplotlib.pyplot as plt


def calculateSN(N):
    SN = 0
    if N == 0:
        return SN
    data = random.choices([-1,1], [0.5,0.5], k=N)
    SN = sum(data)
    return SN

def ecdf(a):
    #Reconstruct the input values from the unique values and counts:
    values, counts = np.unique(a, return_counts=True)

    #Return the cumulative sum of the elements along a given axis
    cuSum = np.cumsum(counts)
    return values, cuSum / cuSum[-1]

def plotEcdf(SNResults, N):
    x, y = ecdf(SNResults)
    x = np.insert(x, 0, x[0])
    y = np.insert(y, 0, 0.)

    plt.plot(x, y, drawstyle = 'steps-post', label = "CDF")
    plt.grid(True)
    plt.xlabel("Values")
    plt.ylabel("P")
    plt.title("CDF & Normal CDF for N = " + str(N))
    plt.legend()
    plt.savefig('CDF&NormalCDF_'+ str(N) + '.png')
    plt.show()

def calculateCDF(N):
    SNResults = []
    
    for i in range(1000):
        result = calculateSN(N)
        SNResults.append(result)
    
    plotEcdf(SNResults, N)

def calculateNormalCDF():
    # create some randomly distributed data:
    data = np.random.randn(1000)

    # sort the data:
    data_sorted = np.sort(data)

    # calculate the proportional values of samples
    p = 1. * np.arange(len(data)) / (len(data) - 1)

    plt.plot(data_sorted, p, label = "Normal CDF")


def start():

    for i in range(5,31, 5):
        calculateNormalCDF()
        calculateCDF(i)

    calculateNormalCDF()
    calculateCDF(100)


start()