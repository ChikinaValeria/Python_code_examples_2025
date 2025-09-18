def get_input(prompt):
    user_input = input(prompt)
    while not user_input.strip():
        print("Characteristic can't be empty")
        user_input = input(prompt)
    return user_input

first_word = get_input("Give the first charactericstic: ")
second_word = get_input("Give the second characteristic: ")
third_word = get_input("Give the third charactericstic: ")
fourth_word = get_input("Give the fourth charactericstic: ")

letter_1 = first_word[0].upper()
letter_2 = second_word[0].upper()
letter_3 = third_word[0].upper()
letter_4 = fourth_word[0].upper()

print(f'{letter_1}.{letter_2}.{letter_3}.{letter_4}.')
