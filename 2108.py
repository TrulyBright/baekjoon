import sys
N = int(sys.stdin.readline())
L = []
summation = 0
for _ in range(N):
  i = int(sys.stdin.readline())
  summation+=i
  L.append(i)

average = summation/N
L.sort()
median = L[(N-1)//2]
count = [0]*8001
for i in L:
  count[i+4000]+=1
maximum=max(count)
modes=[]
for i in range(8001):
  if count[i]==maximum:
    modes.append(i-4000)
modes.sort()
interval = L[-1]-L[0]

print(round(average))
print(median)
print(modes[0] if len(modes)==1 else modes[1])
print(interval)
