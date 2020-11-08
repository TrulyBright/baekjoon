def solution(arr)->list:
  count = [0]*101
  for number in arr:
    count[number]+=1
  for number in count:
    if number!=0 and number!=1:
      result = []
      for i in count:
        if i!=0 and i!=1:
          result.append(i)
      return result
  return [-1]

print(solution(list(map(int, input().split()))))
