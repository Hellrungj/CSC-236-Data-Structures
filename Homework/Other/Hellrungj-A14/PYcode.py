def printDigits(num, base):
    assert(base > 1)
    if(num < base):
        print num
    else:
        printDigits(num / base, base )
        print str(num % base) + " "

def main(): 
    num=0 
    base=0 
    num = input("What is the number to convert: ")
    base = input("What is the new number base for that number: ")
    printDigits(num, base)

if __name__ == '__main__':
    main()
    
    