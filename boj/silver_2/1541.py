# 백준 1541

mod = input()
mod = mod.split("-")
for i in range(len(mod)):
    mod[i] = mod[i].split("+")
    for j in range(len(mod[i])):
        mod[i][j] = int(mod[i][j])
    mod[i] = sum(mod[i])
ans = int(mod[0])
for i in range(1, len(mod)):
    ans -= int(mod[i])
print(ans)
