s = input().strip()

stack = []
count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if s[i-1] == '(':  # 레이저
            count += len(stack)
        else:  # 쇠막대기 끝
            count += 1

print(count)
