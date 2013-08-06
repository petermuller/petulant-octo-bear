"""
interface.py

Classes for interacting with the prime number generator.

@author Peter Muller (pmm5983@rit.edu)
"""

import Tkinter

class CLIInterface:
    """
    Command line wrapper class for interaction with the prime number generator.
    """
    
    def __init__(self,prime,currentState="init",nextState=None):
        self.prime = prime
        self.currentState = currentState
        self.nextState = nextState
        
    def prompt(self):
        """
        Main program flow for the CLI
        States are strings that dictate the program flow.
        """
        run = True
        while (run):
            if self.currentState == "init":
                print "Please enter 'N' to enter Nth Number Mode, 'P' to check"
                print "if a number is prime, or 'E' to exit"
                choice = raw_input().strip()
                if (choice == "N" or choice =="n"):
                    self.nextState = "nth"
                elif (choice == "P" or choice == "p"):
                    self.nextState = "pcheck"
                elif (choice == "E" or choice == "e"):
                    self.nextState = None
                else:
                    print "Error, invalid input."
                    self.nextState = "init"
                print
            elif self.currentState == "nth": #Nth prime number
                try:
                    number = int(input("Enter a value of N to find the Nth "+\
                        "prime number: "))
                    if number < 1:
                        raise
                    result = self.prime.getNthPrime(number)
                    print(str(result))
                    self.nextState = "init"
                except:
                    print "Error, please enter a positive integer."
                    self.nextState = "nth"
                print
            elif self.currentState == "pcheck": #Primeness checker
                try:
                    number = int(input("Enter a number to check its "+\
                        "primeness: "))
                    if self.prime.isPrime(number):
                        print str(number) + " is a prime number!"
                    else:
                        print str(number) + " is not a prime number!"
                    self.nextState = "init"
                except:
                    print "Error, please enter a positive integer."
                    self.nextState = "pcheck"
                print
            else: #If exit or invalid state, then exit
                run = False
            #If any state was entered, it will change state here
            self.currentState = self.nextState

class GUIInterface:
    """
    Graphical wrapper class for interaction with the prime number generator.
    """
    
    def __init__(self,prime,master=None):
        #TODO cleanup, if possible?
        #TODO make windows more user-friendly.
        
        #main window initialization
        self.prime = prime
        master.title("Python-Prime-Gen")
        master.minsize(100,100)
        
        #Inputs
        self.finputs = Tkinter.Frame(master)
        self.finputs.pack()
        self.input1 = Tkinter.Entry(self.finputs,width=40)
        self.input1.insert(Tkinter.INSERT, "Enter a number N for the Nth "+\
            "prime number")
        self.input2 = Tkinter.Entry(self.finputs,width=40)
        self.input2.insert(Tkinter.INSERT, "Enter a number to check its "+\
            "primeness")
        self.input1.pack(side=Tkinter.LEFT)
        self.input2.pack(side=Tkinter.LEFT)
        
        #Buttons
        self.fbuttons = Tkinter.Frame(master)
        self.fbuttons.pack()
        self.submit1 = Tkinter.Button(self.fbuttons,text="Find Nth Prime",\
            command=self.submit1)
        self.submit1.pack(side=Tkinter.LEFT)
        self.ex = Tkinter.Button(self.fbuttons,text="Exit",command=self.quit)
        self.ex.pack(side=Tkinter.LEFT)
        self.submit2 = Tkinter.Button(self.fbuttons,text="Check Primeness",\
            command=self.submit2)
        self.submit2.pack(side=Tkinter.LEFT)
        
        #Results
        self.fresults = Tkinter.Frame(master)
        self.fresults.pack()
        self.answer1 = Tkinter.Text(self.fresults,height=1,width=40)
        self.answer1.pack(side=Tkinter.LEFT)
        self.answer2 = Tkinter.Text(self.fresults,height=1,width=40)
        self.answer2.pack(side=Tkinter.LEFT)
        
        self.master = master
        
    def submit1(self):
        """
        Tells what the Nth prime number is.
        """
        self.answer1.delete('1.0','2.0')
        try:
            number = int(self.input1.get().strip())
            if number < 1:
                raise
            self.answer1.insert(Tkinter.INSERT,\
                str(self.prime.getNthPrime(number)))
        except:
            self.answer1.insert(Tkinter.INSERT,"Error, please enter a"+\
                " positive integer.")
    
    def submit2(self):
        """
        Tells whether or not a number is prime
        """
        self.answer2.delete('1.0','2.0')
        try:
            number = int(self.input2.get().strip())
            if self.prime.isPrime(number):
                self.answer2.insert(Tkinter.INSERT,str(number)+" is a prime" +\
                    " number!")
            else:
                self.answer2.insert(Tkinter.INSERT,str(number)+" is not a "+\
                    "prime number!")
        except:
            self.answer2.insert(Tkinter.INSERT,"Error, please enter a "+\
                "positive integer.")
                
                
    def quit(self):
        """
        Exits the program
        """
        self.master.destroy()
