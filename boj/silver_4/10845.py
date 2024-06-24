import sys

N = int(sys.stdin.readline())
queue_list = []
for i in range(N):
    command = sys.stdin.readline().strip().split(' ')
    if command[0] == 'push':
        queue_list.append(command[1])
    if command[0] == 'pop':
        if len(queue_list) > 0:
            print(queue_list[0])
            del queue_list[0]
        else:
            print(-1)
    if command[0] == 'size':
        print(len(queue_list))
    if command[0] == 'empty':
        if len(queue_list) == 0:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[0])
    if command[0] == 'back':
        if len(queue_list) == 0:
            print(-1)
        else:
            print(queue_list[-1])
    else:
        pass
