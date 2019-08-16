n = 5
k = 1

factorial_list = [1]
for i in range(1, n+1):
    factorial_list.append(factorial_list[i-1] * i)

print(factorial_list[n] / (factorial_list[k] * factorial_list[n-k]))

