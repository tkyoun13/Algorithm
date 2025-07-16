n = int(input())
word = input()
values = [int(input()) for _ in range(n)]

stack = []

for ch in word:
    if ch.isalpha():
        val = values[ord(ch) - ord("A")]
        stack.append(val)
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(a / b)

print('%.2f' %stack[0])