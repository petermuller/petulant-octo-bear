"""
prime.py

The main class for collecting and generating prime number information

@author Peter Muller (pmm5983@rit.edu)
"""

class Prime:
    """
    Class for generating and collecting prime numbers.
    """
    
    def __init__(self):
        self.primesList = [2,3] #known prime numbers to start the list
    
    def primeGen(self,numberToGen):
        """
        Generates the specified number of prime numbers.
        Cycles through previously calculated prime numbers to check primeness of
            the current number, then adds that number to the list if it is prime.
        
        @param numberToGen - Number of prime numbers to generate
        
        @pre - numberToGen is a whole number greater than 0.
        @post - primesList contains at least numberToGen entries.
        """
        i = self.primesList[-1] #current number; last number in current primes list
        index = 0 #index of primes list
        isPrime = True
        while len(self.primesList) < numberToGen:
            while isPrime:
                if index == len(self.primesList):
                    break
                if i % self.primesList[index] == 0:
                    isPrime = False
                index += 1
            if isPrime:
                self.primesList.append(i)
            isPrime = True
            index = 0
            i += 2
        return
    
    def getNthPrime(self,n):
        """
        Returns the Nth prime number. If it wasn't already calculated, the
            method calls the primeGen method to calculate it.
        
        @param n - Index of desired prime number. Note: an n of 1 specifies the
            first number in the list, so that translates to an index of 0 in
            the primesList.
            
        @return number - the Nth prime number
        """
        self.primeGen(n) #if n < len(self.primesList): return
        return self.primesList[n-1]