import pyfiglet

logo = pyfiglet.figlet_format("Multiple Table")
print(logo)
for k in range(1, 13):
    print(k, end="\t")

print("\n-------------------------------------------------------------------------------------------")
# print("________GOOD LUCK______________\n")

for j in range(1, 13):
    for k in range(1, 13):
        print(j * k, end="\t")
    print("\n")
