A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))
D = [0, 0]

if A[1]==B[1]:
  D[1]=C[1]
elif A[1]==C[1]:
  D[1]=B[1]
else:
  D[1]=A[1]

if A[0]==B[0]:
  D[0]=C[0]
elif A[0]==C[0]:
  D[0]=B[0]
else:
  D[0]=A[0]
print(*D)
