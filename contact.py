with open('contact.txt', 'r') as f:
    data = f.readlines()
    f.close()

# print(data)

for i,line in enumerate(data, 1):
    # print(i, line)
    # print(len(line))

    if i == 1:
        print(line)
    