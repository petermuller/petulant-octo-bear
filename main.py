"""
main.py

Includes the main program flow for the petulant-octo-bear program.

@author Peter Muller (pmm5983@rit.edu)
"""

def primeGen(primesList,numberToGen):
    """
    Generates the specified number of prime numbers.
    Cycles through previously calculated prime numbers to check primeness of
        the current number
    
    @param primesList - Current array of prime numbers
    @param numberToGen - Number of prime numbers to generate
    
    @return pl - Updated array of prime numbers
    
    @pre - primesList is not empty
    @pre - numberToGen is a whole number greater than 0.
    """
    pl = primesList
    i = pl[-1] #current number; last number in current primes list
    index = 0 #index of primes list
    isPrime = True
    while len(pl) < numberToGen:
        while isPrime:
            if index == len(pl):
                break
            if i % pl[index] == 0:
                isPrime = False
            index += 1
        if isPrime:
            pl.append(i)
        isPrime = True
        index = 0
        i += 2
    return pl
    
def getNthPrime(n):
    return pl[n-1]
    
def main():
    #TODO convert this to O-O style.
    primesList = [2,3]
    pass
    
if __name__ == "__main__":
    main()
