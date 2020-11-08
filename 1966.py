import queue
T = int(input())
for _ in range(T):
  Q = queue.Queue()
  N, M = map(int, input().split())
  priority = list(map(int, input().split()))
  isPrinted = [False]*N
  for i in range(N):
    Q.put(i)
  count = 0
  while not Q.empty():
    front = Q.get()
    priorityOfFront = priority[front]
    for i, p in enumerate(priority):
      if priorityOfFront<p and not isPrinted[i]:
        Q.put(front)
        break
    else: # print front
      isPrinted[front]=True
      count+=1
      if front==M:
        print(count)
        break
