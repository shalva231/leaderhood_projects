names = []

for i in range(5):
    name = input("Type your name: ")
    names.append(name)

count = 0

for name in names:
    if name == "luka":
       count += 1

print(count)
