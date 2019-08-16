li = [1,2,3]
k = 4


def countChange(n, coin_list):

    def accumulate(acc, toBeTried):
        if acc == n:
            return 1
        elif acc > n or len(toBeTried) == 0:
            return 0
        else:
            return accumulate(acc + toBeTried[0], toBeTried) + accumulate(acc, toBeTried[1:])

    if n == 0:
        return 0
    else:
        return accumulate(0, coin_list)


print(countChange(k, li))