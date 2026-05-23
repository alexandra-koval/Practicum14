n = int(input())
dictionary = {}

for i in range(n):
    line = input().split()
    form = line[0]
    items = []
    for word in line[1:]:
        items.append(word)
    dictionary[form] = items

target = input()

for form, items in dictionary.items():
    if target in items:
        print(form)
