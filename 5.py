name = {}
n = int(input())
for i in range(n):
    parents, kid = input().split()
    if parents in name:
        name[parents].append(kid)
    else:
        name[parents] = [kid]


def count(names):
    if names not in name.keys():
        return 0
    kids = name.get(names)
    return len(kids) + sum([count(a) for a in kids])


print(count(input()))
