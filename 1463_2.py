N = int(input())

minimum = 10**6
def DFS(n, count):
  global minimum
  if count>minimum:
    return
  if n==1:
    minimum = count
    return
  if n%3==0: DFS(n//3, count+1)
  if n%2==0: DFS(n//2, count+1)
  DFS(n-1, count+1)

DFS(N, 0)
print(minimum)
