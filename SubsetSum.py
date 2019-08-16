n = 9


def isSubsetSum(acc, toBeTried):
    if acc == n or len(toBeTried) == 0:
        return True
    elif acc > n:
        return False
    else:
        return isSubsetSum(acc + toBeTried[0], toBeTried[1:]) or isSubsetSum(acc, toBeTried[1:])


arr = [3, 34, 4, 12, 5, 2]
print (isSubsetSum(0, arr))