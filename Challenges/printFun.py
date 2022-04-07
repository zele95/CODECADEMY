# Recursion visualisation
 
def printFun(test):
    if test < 1:
        return
    else:
        print(test)
        printFun(test-1)
        print(test)
        return
        

printFun(3)