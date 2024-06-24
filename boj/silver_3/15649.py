def sol(arr, result, M):
  if len(result) == M:
    for el in result:
      print(el, end=' ')
    print()
    return
  for index in range(len(arr)):
    el = arr[index]
    rest = arr[0:index]+arr[index+1:]
    sol(rest, result+[el], M)


N, M = map(int, input().split(' '))
sol(list(range(1, N+1)), [], M)
