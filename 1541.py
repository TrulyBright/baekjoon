expression = list(input())

# 수 앞에 붙은 0 지우기
if len(expression)>=2 and expression[1].isdigit() and expression[0]=='0':
  expression[0]=''
for i in range(2, len(expression)):
  if expression[i].isdigit() and expression[i-1]=='0' and not expression[i-2].isdigit():
    expression[i-1]=''

# 괄호 넣기
i=0
while i<len(expression):
  if expression[i]=='-':
    expression.insert(i+1, '(')
    j=i+1
    while j<len(expression) and expression[j]!='-':
      j+=1
    expression.insert(j, ')')
  i+=1
print(eval(''.join(expression)))
