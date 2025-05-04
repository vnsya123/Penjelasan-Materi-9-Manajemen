handle = open('data.txt','w')

count = 0
for line in handle:
    if len(line.strip()) > 0 :
        count += 1

print(count)