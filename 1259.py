N = int(input())
while N!=0:
  L = list(str(N))
  for i in range(len(L)):
    if L[i]!=L[len(L)-i-1]:
      print("no")
      break
  else:
    print("yes")
  N=int(input())
