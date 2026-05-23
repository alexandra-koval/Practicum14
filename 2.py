n = int(input())
dictionary = {}

for i in range(n):
    rus, eng = input().split()
    dictionary[rus] = eng

text = input().split()

for word in text:
    if word in dictionary:
        print(dictionary[word], end=' ')
    else:
        print(word, end=' ')
