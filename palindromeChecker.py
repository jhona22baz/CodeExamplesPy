from deque import Deque

def palindromeChecker(word):
    charDeque = Deque()
    
    for ch in word:
        charDeque.addRear(ch)
    
    stillEqual = True
    
    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False
            
    return stillEqual
    
    
print(palindromeChecker('anitalavalatina'))
print(palindromeChecker('rar'))
print(palindromeChecker('location'))
