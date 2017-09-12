def odd(k,s,t):
    # s = start position
    # t = target position
    # o = on hand position
    o = 6 - s - t
    if k == 1:
        list = [[s,t]]
        return list
    else:
        list = odd(k-1,s,t) + [[s,o]] + odd(k-1,t,o) + [[s,t]] + odd(k-1,o,s) + [[o,t]] + odd(k-1,s,t)
        return list

def even(k,s,t):
    # s = start position
    # t = target position
    # o = on hand position
    o = 6 - s - t
    if k == 1:
        list = [[s,o],[s,t],[o,t]]
        return list
    else:
        list = even(k-1,s,t) + [[s,o]] + even(k-1,t,o) + [[s,t]] + even(k-1,o,s) + [[o,t]] + even(k-1,s,t)
        return list

def hanoi(n):
    if n%2==1:
        k = (n+1)//2
        answer = odd(k,1,3)
    else:
        k = n//2
        answer = even(k,1,3)
    return answer  # 2차원 배열을 반환해 주어야 합니다.


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(hanoi(3))
