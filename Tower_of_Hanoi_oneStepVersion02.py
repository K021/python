
import time
startTime = time.time()

def hanoi(n,start=1,target=3):  #default value

    onHand = 6 - start - target #able to change the positions

    if n == 1:
        trace = [[start,target]]
        return trace
    else:
        trace1 = hanoi(n-1,start,onHand)  #trace of the top series
        trace2 = [[start,target]]         #trace of the bottom
        trace3 = hanoi(n-1,onHand,target) #trace of the top series
        trace = trace1 + trace2 + trace3
        return trace

print(hanoi(22))

endTime = time.time() - startTime
print(endTime)
