tree = {}
n = int(input())

for i in range(n):
    parent, child = input().split()
    if parent in tree:
        tree[parent].append(child)
    else:
        tree[parent] = [child]


def count(name):
    """Return the total number of descendants for a given person."""
    if name not in tree:
        return 0
    children = tree.get(name)
    return len(children) + sum([count(child) for child in children])


print(count(input()))
