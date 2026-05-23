n = int(input())
a = {}
for i in range(n):
    b = input().split()
    form = b[0]
    d = []
    for word in b[1:]:
        d.append(word)
    a[form] = d
word = input()
for k, v in a.items():
    if word in v:
        print(k)
