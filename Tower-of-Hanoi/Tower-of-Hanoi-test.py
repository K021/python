    arr.sort()
    if arr[-1] == len(arr):
        return True
    else:
        return False

    for i in range(len(arr)):
        if i+1 not in arr:
            return False
    return True
