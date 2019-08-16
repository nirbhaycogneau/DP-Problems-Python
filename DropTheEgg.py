def max(x, y):
    return x if x > y else y


def maximumSub(acc, toBeTried, n,  max):
    if acc > max:
        return acc
    elif len(toBeTried) == 0:
        return max
    else:
        return maximumSub(acc, toBeTried[n:])
