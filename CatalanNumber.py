catalan_list = []
k = 8


def get_catalan_list(n):
    if n == 0:
        return 1
    elif n < len(catalan_list):
        return catalan_list[n]
    else:
        s = 0
        for i in range(0, n):
            s = s + get_catalan_list(i) * get_catalan_list(n-i-1)
        return s


for i in range(0, k):
    catalan_list.append(get_catalan_list(i))
print(catalan_list)
