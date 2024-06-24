input()
arr = list(map(int, input().split(' ')))
'''
모든 수는 절댓값이 100이하!!!
1 4 13 40

예시 항이 1개 -> 무조건 A
예시 항이 2개 -> 두 값이 같으면 그값 아니면 A

3개 이상일때
무한으로 보냈을 때 수렴하면 안됨X 무조건 발산해야함!!!!
즉 |N(2)-N(1)| >= |N(3)-N(2)| 이 아니면 B

1 8 19
7 11
'''
if len(arr) == 1:
    print('A')

elif len(arr) == 2:
    if arr[0] != arr[1]:
        print('A')
    else:
        print(arr[0])

else:
    if (arr[0] - arr[1] == 0):
        a = 0
    else:
        a = (arr[1] - arr[2]) // (arr[0] - arr[1])
    b = arr[1] - arr[0] * a
    for i in range(len(arr) - 1):
        expect = arr[i] * a + b  # 다음 예측값
        if (arr[i + 1] != expect):  # 예측값과 실제가 다르다면
            print('B')
            exit()
    print(arr[-1] * a + b)
