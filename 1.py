s = input().split()
a = {}
for i in s:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
words = sorted(a.items(), key=lambda x: x[1], reverse=True)
for i in words:
    print(i[0])
