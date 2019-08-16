maxWeight = 50
arr = [(100, 20), (60, 10), (120, 30)]


def max(x, y):
    if x > y:
        return x
    else:
        return y


def knapsack(accCal, accWeight, toBeTried, maxCal):
    if accWeight == maxWeight:
        print (toBeTried)
        print(accCal)
        return max(accCal, maxCal)
    elif len(toBeTried) == 0:
        print (toBeTried)
        if accWeight < maxWeight:
            print (max(accCal, maxCal))
            return max(accCal, maxCal)
        else:
            print(maxCal)
            return maxCal
    elif accWeight > maxWeight:
        return knapsack(accCal - toBeTried[0][0], accWeight - toBeTried[0][1], toBeTried[1:], maxCal)
    else:
        print (toBeTried)
        print(accCal)
        return knapsack(accCal, accWeight, toBeTried[1:],
                 max(knapsack(accCal + toBeTried[0][0], accWeight + toBeTried[0][1], toBeTried[1:], maxCal), maxCal))


print(knapsack(0, 0, arr, 0))
