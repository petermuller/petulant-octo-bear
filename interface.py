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
    
    def __init__(self,prime):
        self.prime = prime
        
    def prompt(self):
        """
        Main program flow for the CLI
        """
        run = True
        while (run):
            try:
                number = int(input("Enter a value of N to find the Nth prime number: "))
                result = self.prime.getNthPrime(number)
                print(str(result))
            except:
                print("Error, please enter a positive integer.")
            print
            again = raw_input("Type 'e' to exit, or press Enter to try again. ").strip()
            if again == 'e':
                run = False
            print
    
class GUIInterface:
    """
    Graphical wrapper class for interaction with the prime number generator.
    """
    
    def __init__(self,prime,master=None):
        self.prime = prime
        master.title("Petulant-Octo-Bear")
        master.minsize(100,100)
        self.instructions = Tkinter.Text(master,height=1)
        self.instructions.insert(Tkinter.INSERT, "Enter a number N for the Nth prime number")
        self.instructions.pack(fill='x')
        self.input = Tkinter.Entry(master)
        self.input.pack(fill='x')
        self.submit = Tkinter.Button(master,text="Submit",command=self.submit)
        self.submit.pack()
        self.ex = Tkinter.Button(master,text="Exit",command=self.quit)
        self.ex.pack()
        self.answer = Tkinter.Text(master,height=1)
        self.answer.pack()
        self.master = master
        
    def submit(self):
        """
        Gets input and sets the output
        """
        try:
            number = int(self.input.get().strip())
            if number < 1:
                raise
            self.answer.delete('1.0','2.0')
            self.answer.insert(Tkinter.INSERT,str(self.prime.getNthPrime(number)))
        except:
            self.answer.delete('1.0','2.0')
            self.answer.insert(Tkinter.INSERT,"Error, please enter a positive integer.")
        
    def quit(self):
        """
        Exits the program
        """
        self.master.destroy()