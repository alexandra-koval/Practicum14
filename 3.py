n = int(input())
a = {}
for i in range(n):
    word1, word2 = input().split()
    a[word1] = word2
word = input()
if word in a:
    print(a[word])
else:
    print(word)
