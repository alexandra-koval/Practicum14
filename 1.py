text = input().split()
count = {}

for word in text:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

result = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word, num in result:
    print(word)
