name = input("Enter a name: ")
name = name.lower()

for index, letter in enumerate(name):
    position = ord(letter) - ord('a') + 1
    print(f"The position of '{letter}' in the name is {position}")
