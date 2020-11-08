N = int(input())
stat = []
for _ in range(N):
  stat.append(list(map(int, input().split())))

def statOf(team)->int:
  result = 0
  for i in team:
    for j in team:
      result+=stat[i][j]
  return result
everyone = set(range(0, N))
combinations = []
picked = []

def pick(count):
  if count==N//2:
    combinations.append(set(picked))
    return
  for i in range(0 if not picked else picked[-1]+1, N):
    picked.append(i)
    pick(count+1)
    picked.remove(i)
pick(0)
minimum = 100*2*20
for c in combinations:
  minimum = min(minimum, abs(statOf(c)-statOf(everyone-c)))
print(minimum)
