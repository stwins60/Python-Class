pig_latin = str(input("Enter a sentence: "))

words = pig_latin.split()

for word in words:
    print(word[1:])
    print(word[1:] + word[0] + "ay", end = " ")

print(words)