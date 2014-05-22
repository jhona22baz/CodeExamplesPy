from stack import Stack

def divideBy2(decimalNumber):
    remstack = Stack()
    
    while decimalNumber > 0:
        rem = decimalNumber%2
        remstack.push(rem)
        decimalNumber = decimalNumber//2
        
    
    binaryString = ""
    while not remstack.isEmpty():
        binaryString = binaryString + str(remstack.pop())
        
    return binaryString
    
    
print (divideBy2(45))
    
