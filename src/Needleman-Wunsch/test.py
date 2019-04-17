from NeedleWunsch import NeedleWunsch as NW
from termcolor import colored
nw = NW("GCATG-CU", "G-ATTACA")
# print(colored(nw, "blue"))
nw.run()
print(colored('''Needleman-Wunsch Algorithm \
table for strings: "GCATG-CU" and "G-ATTACA" is:''', "yellow"))
print(colored(nw,color="green"))