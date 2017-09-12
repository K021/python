def hanoi(n):
    answer = []
    answer = move(n,answer,1,3)
    return answer

def move(n,trace,start,target):
    onHand = 6 - start - target
    if n == 1:
        trace = [start,target]
        return trace
    else:
        trace1 = move(n-1,trace,start,onHand)
        trace2 = [start,target]
        trace3 = move(n-1,trace,onHand,target)
        trace = trace1 + trace2 + trace3
        return trace

print(hanoi(3))
