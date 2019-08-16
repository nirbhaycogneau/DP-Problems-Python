arr = [(1,1),(2,45),(3,8),(4,9),(5,110),(6,17),(7,17),(8,20)]


def max(x, y):
    if x > y:
        return x
    else:
        return y


def optimumCut(acc, toBeTried, l, maxAcc ):
    print(toBeTried)
    print(acc)
    print(l)
    if l == 0 or len(toBeTried) == 0:
        return max(acc, maxAcc)
    elif l < 0:
        return optimumCut(acc - toBeTried[0][1], toBeTried[1:], l + toBeTried[0][0], maxAcc)
    else:
        # return max(optimumCut(acc+toBeTried[0][1], toBeTried, l - toBeTried[0][0], maxAcc),
        #            optimumCut(acc, toBeTried[1:], l, maxAcc))
        return optimumCut(acc, toBeTried[1:], l, max(optimumCut(acc+toBeTried[0][1], toBeTried, l - toBeTried[0][0], maxAcc), maxAcc))


print(optimumCut(0, arr[::-1], 8, 0))

