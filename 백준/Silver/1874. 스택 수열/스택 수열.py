n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1 # stack에 push할 숫자 (1부터 시작)
possible = True

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append('+') # + -> push
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-') # - -> pop
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print('NO')