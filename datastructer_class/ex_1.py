def find_first_duplicate(input_str):
    seen_letters = set()
    for char in input_str:
        if char in seen_letters:
            return char
        seen_letters.add(char)
    return None

input_str =input("enter the string : ")
first_duplicate = find_first_duplicate(input_str)

print("The first duplicate letter is:", first_duplicate)
