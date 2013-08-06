"""
main.py

Includes the main program flow for the python-prime-gen program.

@author Peter Muller (pmm5983@rit.edu)
"""

import interface
import prime
import sys
import Tkinter

def main():
    p = prime.Prime()
    if len(sys.argv) == 1:
        root = Tkinter.Tk()
        iface = interface.GUIInterface(p,root)
        root.mainloop()
    elif sys.argv[1] == "-c":
        iface = interface.CLIInterface(p)
        iface.prompt()
    else:
        print "Usage: python main.py [-c]"
    exit()
    
if __name__ == "__main__":
    main()
