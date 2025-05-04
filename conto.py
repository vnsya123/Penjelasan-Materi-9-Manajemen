handle = open('data.txt')

count = 0
for line in handle:
    count += 1

print(count)