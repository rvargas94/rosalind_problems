######################################
#This script will solve the problem  #
#Mendel's First Law                  #
#From http://rosalind.info/problems  #
######################################

import numpy as np

#k individuals are homozygous dominant for a factor, 
#m are heterozygous,
#n are homozygous recessive.
#This function will not work if m or n is 0
def solve(k,m,n):
    assert(m > 0 and n > 0)

    #solve for compliment. (Not sure if needed)
    populationSize = k+m+n

    #This will calculate following
    #Pr(X is n and Y is n) +
    #Pr(X is n and Y is m and Y is recessive)
    #Pr(X is m and X is recessive and Y is n) +
    #Pr(X is m and X is recessive and Y is m and Y is recessive)
    probability = (
        (n/populationSize) * ((n-1)/(populationSize-1)) +
        (n / populationSize) * (m / (populationSize-1)) * .5 +
        (m/populationSize) * .5 * (n/(populationSize-1)) +
        (m/populationSize) * ((m-1)/(populationSize-1)) * 0.25
    )
    return 1 - probability

def main():
    debug = True
    
    #Assign k,m,n here.
    k = 0
    m = 0
    n = 0

    if(debug):
        k = 2
        m = 2
        n = 2
    
    probability = solve(k,m,n)
    
    if(debug):
        np.testing.assert_almost_equal(probability,0.78333,5)

if __name__ == '__main__':
    main()
