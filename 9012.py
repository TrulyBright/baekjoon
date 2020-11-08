T = int(input())
for _ in range(T):
  S = input()
  stack = []
  for p in S:
    if p=='(':
      stack.append(p)
    else:
      if len(stack)==0:
        print("NO")
        break
      if stack[-1]=='(':
        stack.pop()
  else:
    print("YES" if len(stack)==0 else "NO")
