# JO 2858
# https://bit.ly/2JRxFgx

arr = list(input())

bar, pec = 0, 0
for i in range(len(arr)):
    if arr[i] == '(':
        bar += 1
    else:
        bar -= 1
        if arr[i-1] == '(':
            pec += bar
        else:
            pec += 1

print(pec)