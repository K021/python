def hanoi(n):
    answer = []
    answer = move(n,answer,1,3)
    return answer

def move(n,trace,start,target):
    onHand = 6 - start - target
    if n == 1:
        trace.append([start,target])
        return trace
    else:
        trace = move(n-1,trace,start,onHand)
        trace.append([start,target])
        trace = move(n-1,trace,onHand,target)
        return trace
