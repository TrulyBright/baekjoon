S = input()
while S!='.':
  stack = []
  for c in S:
    if c=='[' or c=='(':
      stack.append(c)
    elif c==')':
      if len(stack)==0 or stack[-1]!='(':
        print("no")
        break
      stack.pop()
    elif c==']':
      if len(stack)==0 or stack[-1]!='[':
        print("no")
        break
      stack.pop()
  else:
    print("yes" if len(stack)==0 else "no")
  S = input()
