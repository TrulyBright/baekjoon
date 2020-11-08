N = int(input())
W = [0]*N
for i in range(N):
  W[i]=list(map(int, input().split()))

minimum = 1000000*15
visited = [False]*N
def visit(cost, startCity, currentCity):
  global minimum
  if cost>minimum:
    return
  if False not in visited:
    minimum = min(minimum, cost+W[currentCity][startCity])
    return

  for destination in range(N):
    if W[currentCity][destination]!=0 and not visited[destination]:
      visited[destination]=True
      visit(cost+W[currentCity][destination], startCity, destination)
      visited[destination]=False

for startCity in range(N):
  visited[startCity]=True
  visit(0, startCity, startCity)
  visited[startCity]=False

print(minimum, count)
