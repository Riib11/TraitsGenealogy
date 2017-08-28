import examples
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if(len(args) == 1): # must be example by name
        ex = examples.examples[args[0].upper()]
        if(ex): ex()
        else: print("[!] example not avaliable")
    elif(len(args) == 7 or len(args) == 6):
        examples.custom(args)
    else:
        print("[!] incorrect number of arguments")