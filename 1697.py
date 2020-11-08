import queue
N, K = map(int, input().split())
visited = [False]*100001

def notOutOfLine(x):
  return 0<=x and x<=100000

Q = queue.Queue()
Q.put((N, 0))
visited[N]=True
result = 100000
while not Q.empty():
  v = Q.get()
  # print(v)
  current = v[0]
  time = v[1]
  if current==K:
    result = min(result, time)
  if time>result:
    continue
  if notOutOfLine(2*current) and not visited[2*current]:
    Q.put((2*current, time+1))
    visited[2*current]=True
  if notOutOfLine(current-1) and not visited[current-1]:
    Q.put((current-1, time+1))
    visited[current-1]=True
  if notOutOfLine(current+1) and not visited[current+1]:
    Q.put((current+1, time+1))
    visited[current+1]=True

print(result)
