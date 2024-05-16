name = input("enter any name")
name = name.lower()
letter_count ={}
for letter in name:
    if letter.isalpha():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
for letter, count in letter_count.items():
    print(f"the alphabet '{letter}' appears {count} times in the name")            