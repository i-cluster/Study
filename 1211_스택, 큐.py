# JO 1102, JO 1697
# https://bit.ly/3418f6E, https://bit.ly/2Kk4LFi

stack = []
que = []

for _ in range(int(input())):
    inp = input().split()
    if inp[0] == 'i':
        stack.append(inp[1])
        que.append(inp[1])
    elif inp[0] == 'o':
        if stack:
            print(stack.pop())
        else:
            print('empty')
        if que:
            print(que.pop(0))
        else:
            print('empty')
    else:
        print(len(stack))
        print(len(que))