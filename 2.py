n = int(input())
a = {}
for i in range(n):
    rus, eng = input().split()
    a[rus] = eng
s = input().split()
for word in s:
    if word in a:
        print(a[word], end=' ')
    else:
        print(word, end=' ')
