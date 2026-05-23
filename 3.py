n = int(input())
dictionary = {}

for i in range(n):
    word1, word2 = input().split()
    dictionary[word1] = word2

word = input()

if word in dictionary:
    print(dictionary[word])
else:
    print(word)
