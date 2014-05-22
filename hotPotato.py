from queue import Queue

def hotPotatoe(nameList, num):
    simqueue = Queue()
    for name in nameList:
        simqueue.enqueue(name)
    
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
            simqueue.saw()    
        simqueue.dequeue()
       
    return simqueue.dequeue()
    
print (hotPotatoe(["Bill","David","Susan","Jane","Kent","Brad"],7))