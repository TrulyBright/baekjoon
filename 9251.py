A = '0' + input()
lenA = len(A)
B = '0' + input()
lenB = len(B)
D = [[0]*lenB for _ in range(lenA)]
# D[i][j] = A[:i+1]과 B[:j+1]의 LCS의 길이
# D[i][j] = D[i-1][j-1]+1 if A[i]==B[i]
for i in range(1, lenA):
  for j in range(1, lenB):
    # print(A[1:i+1], B[1:j+1])
    if A[i]==B[j]:
      D[i][j] = D[i-1][j-1]+1
    else:
      # print(i, j)
      D[i][j] = max(D[i][j-1], D[i-1][j])
maximum = 0
for i in D:
  maximum = max(maximum, max(i))
print(maximum)
