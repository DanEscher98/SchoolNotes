import os
import regex
import string
from math import trunc
from random import choice

vectorDict = {}

def stringValidation(string, pattern):
    pattern = regex.compile(pattern)
    return bool(pattern.match(string))

class Switcher:
    def selector(self, x):
        if(x>1 and not bool(vectorDict)):
            print("You don't have enough vectors")
            input("\nPress [Enter] to continue.")
        else:
            method = getattr(self,'op_'+str(x),lambda :'Invalid')
            return method()

    def op_0(self):
        print("Goodbye...")
        input("\nPress [Enter] to continue.")

    def op_1(self):
        num = int(input("How many vectors will you add?: "))
        for i in range(num):
            vector = []
            while(True):
                name = choice(string.ascii_uppercase)
                if(not name in vectorDict): break
            while(True):
                strList = input("Values for vector "+name+": ").split(' ')
                for n in strList:
                    if stringValidation(n, "^-?[0-9]*(\.[0-9]+)?$"):
                        valid = True
                        n = float(n)
                        if(n==trunc(n)):
                            n = int(n)
                        n = vector.append(n)
                    else:
                        print("Set only valid numbers!")
                        valid = False
                        break
                if(valid):break
            vectorDict[name] = vector

    def op_2(self):
        for key in vectorDict:
            print(key + ": ", vectorDict[key])
        input("\nPress [Enter] to continue.")

    def op_3(self):
        while(True):
            os.system("clear")
            for key in vectorDict:
                print(key + ": ", vectorDict[key])
            while(True):
                key = input("Select a vector to erease: ")
                if key in vectorDict:
                    del vectorDict[key]
                    break
                else:
                    print("That vector doesn't exist.")

            if(vectorDict):
                if(not input("Erease another? [y/n]: ")=='y'): break
            else: break


if __name__=='__main__':
    while(True):
        os.system("clear")
        print("[1] Add new vector")
        if(bool(vectorDict)):
            print("[2] Print vectors")
            print("[3] Delete vectors")
        print("[0] Finish program")

        x = int(input("Choose an option: "))
        print("")
        Switcher().selector(x)
        if(x==0): break
    os.system("clear")