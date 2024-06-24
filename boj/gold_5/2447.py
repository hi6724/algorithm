def sol(n):
  if n == 3:
    return ['***', '* *', '***']
  pattern = []
  arr = sol(n//3)
  for i in arr:
    pattern.append(i*3)

  for i in arr:
    pattern.append(i+' '*(n//3)+i)

  for i in arr:
    pattern.append(i*3)

  return pattern


N = int(input())
result = sol(N)
for i in result:
  print(''.join(i))
