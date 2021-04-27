#!/bin/bash/python
""" WordListGen is a program designed to assist a user in creating wordlists that may
be used with Hashcat - the Kali-Linux Password Cracking Utility. A user user can choose 
to combine up to three lists of words together to form a comprehensive wordlist. A numeric value
can also be concatenated to the wordlist. This is determined by a range which is set by the user.
The numeric value can be placed at the beginning or end of the concatenated words. A user must
enter each wordlist in the order they should be concatenated.
"""
import sys

# create a function that will remove individual words from a text document, it will remove
# whitespace in front of and behind words, and the add each individual word to a list.
def load_words(filename):
    individual_words = list()

    with open(filename) as lines:
        for line in lines:
            individual_words.append(line.strip())
        return individual_words


not_a_valid_integer = "The input given is not a valid integer.\n"
is_valid_input = False

# Ask the user for how many wordlists they would like to combine, this requires an integer as input.
# If an integer is not provided, I catch the exception, print a statement, and reprompt the user.
while is_valid_input == False:
    try:
        number_of_wordlists_to_combine = int(input("Please enter the number of wordlists you would " \
        "like to combine: "))
        if 1 <= number_of_wordlists_to_combine <=3:
            is_valid_input = True
        else:
            print(not_a_valid_integer)
            continue
    except ValueError:
        print(not_a_valid_integer)

# This series of if/elif statements gets the absolute path of each wordlist to be pulled
# The provided wordlists are sent to the load_words function.
if number_of_wordlists_to_combine == 1:
    first_wordlist_location = input("Please provide the absolute path to the wordlist: ")
elif number_of_wordlists_to_combine == 2:
    first_wordlist_location = input("Please provide the absolute path to the first wordlist: ")
    second_wordlist_location = input("Please provide the absolute path to the second wordlist: ")
else:
    first_wordlist_location = input("Please provide the absolute path to the first wordlist: ")
    second_wordlist_location = input("Please provide the absolute path to the second wordlist: ")
    third_wordlist_location = input("Please provide the absolute path to the third wordlist: ")


is_valid_input = False

# Prompt the user for input by asking if they would like to add numbers to the generated wordlist.
# The input must either be 'y' or 'n', otherwise a statement is printed and they are reprompted.
while is_valid_input == False:
    user_wants_add_number = input("Would you like to concatenate numeric values to the word(s), Y/N? ")
    user_wants_add_number = user_wants_add_number.lower()
    if user_wants_add_number == 'y' or user_wants_add_number == 'n':
        is_valid_input = True
    else:
        print("That's invalid, please enter either 'Y' or 'N'.\n")

# Exit program if the user input for number of wordlists is one and user input for adding numbers is no.
if number_of_wordlists_to_combine == 1 and user_wants_add_number == 'n':
    message = ("\nYou already have a list! :P\n")
    message += ("Perhaps you should try running this program again while using different options?")
    print(message)
    sys.exit()

# If the user wants to concatenate numbers to the generated wordlist, I prompt to ask them where.
# If the user doesn't enter 'beginning' or 'end', a statement is printed, and they are reprompted.
if user_wants_add_number == 'y':
    is_valid_input = False
    while is_valid_input == False:
            where_add_number = input("Where would you like to concatenate the numbers? " \
                "Please enter 'beginning' or 'end': ")
            where_add_number = where_add_number.lower()
            if where_add_number == 'beginning' or where_add_number == 'end':
                is_valid_input = True
            else:
                print("That's invalid, please enter 'beginning' or 'end'.\n")



# If user wants to add numeric values to passwords, ask for user input to get the starting and 
# ending range values. If 'y' or 'n' isn't entered, print a statement and reprompt.
if user_wants_add_number == 'y':
    is_valid_input = False
    while is_valid_input == False:
            try:
                starting_range_value = int(input("Please enter the starting value of the numeric range: "))
                is_valid_input = True
            except ValueError:
                print:(not_a_valid_integer)
            try:
                ending_range_value = int(input("Please enter the ending value of the numeric range: "))
            except:
                print(not_a_valid_integer)


# Ask the user if the pin need to have a fixed length pin. Accept only 'y' and 'n' as answers.
# If an inappropriate response is given, print statement and reprompt.
if user_wants_add_number == 'y':
    is_valid_input = False
    while is_valid_input == False:
        preceeding_example_one = 1
        preceeding_example_two = 2
        preceeding_example_three = 3 
        user_wants_preceeding_zeroes = input("Does the pin need to contain preceeding zeroes, Y/N? " \
            f"Example: {str(preceeding_example_one).zfill(len(str(ending_range_value)))}, " \
                f"{str(preceeding_example_two).zfill(len(str(ending_range_value)))}, " \
                    f"{str(preceeding_example_three).zfill(len(str(ending_range_value)))}: ")
        user_wants_preceeding_zeroes = user_wants_preceeding_zeroes.lower()
        if user_wants_preceeding_zeroes == 'y' or user_wants_preceeding_zeroes == 'n':
            is_valid_input = True
        else:
            print("That's invalid, please enter either 'Y' or 'N'.\n")


# def one_wordlist_add_number_preceeding_zeroes():
#     for word in first_wordlist:
#         for pin in range(starting_range_value, ending_range_value + 1):
#             potential_password = f"{str(pin)}"


final_wordlist = list()
# This block of code is where the final wordlists are generated. I plan to refactor this code so that code is not
# repeated as much!
if number_of_wordlists_to_combine == 1 and user_wants_add_number == 'y' and user_wants_preceeding_zeroes == 'y':
    first_wordlist = load_words(first_wordlist_location)
    if where_add_number == 'beginning':
        for word in first_wordlist:
            for pin in range(starting_range_value, ending_range_value + 1):
                potential_password = str(pin).zfill(len(str(ending_range_value))) + word
                final_wordlist.append(potential_password)
    elif where_add_number == 'end':
        for word in first_wordlist:
            for pin in range(starting_range_value, ending_range_value + 1):
                potential_password = word + str(pin).zfill(len(str(ending_range_value)))
                final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 1 and user_wants_add_number == 'y' and user_wants_preceeding_zeroes == 'n':
    first_wordlist = load_words(first_wordlist_location)
    if where_add_number == 'beginning':
        for word in first_wordlist:
            for pin in range(starting_range_value, ending_range_value + 1):
                potential_password = str(pin) + word
                final_wordlist.append(potential_password)
    elif where_add_number == 'end':
        for word in first_wordlist:
            for pin in range(starting_range_value, ending_range_value + 1):
                potential_password = word + str(pin)
                final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 2 and user_wants_add_number == 'y' and user_wants_preceeding_zeroes == 'y':
    first_wordlist = load_words(first_wordlist_location)
    second_wordlist = load_words(second_wordlist_location)
    if where_add_number == 'beginning':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for pin in range(starting_range_value, ending_range_value + 1):
                    potential_password = str(pin).zfill(len(str(ending_range_value))) + first_word + second_word
                    final_wordlist.append(potential_password)
    elif where_add_number == 'end':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for pin in range(starting_range_value, ending_range_value + 1):
                    potential_password = first_word + second_word + str(pin).zfill(len(str(ending_range_value)))
                    final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 2 and user_wants_add_number == 'y' and user_wants_preceeding_zeroes == 'n':
    first_wordlist = load_words(first_wordlist_location)
    second_wordlist = load_words(second_wordlist_location)
    if where_add_number == 'beginning':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for pin in range(starting_range_value, ending_range_value + 1):
                    potential_password = str(pin) + first_word + second_word
                    final_wordlist.append(potential_password)
    elif where_add_number == 'end':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for pin in range(starting_range_value, ending_range_value + 1):
                    potential_password = first_word + second_word + str(pin)
                    final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 2 and user_wants_add_number == 'n':
    first_wordlist = load_words(first_wordlist_location)
    second_wordlist = load_words(second_wordlist_location)
    for first_word in first_wordlist:
        for second_word in second_wordlist:
            potential_password = first_word + second_word
            final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 3 and user_wants_add_number == 'y' and user_wants_preceeding_zeroes == 'y':
    first_wordlist = load_words(first_wordlist_location)
    second_wordlist = load_words(second_wordlist_location)
    third_wordlist = load_words(third_wordlist_location)
    if where_add_number == 'beginning':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for third_word in third_wordlist:
                    for pin in range(starting_range_value, ending_range_value + 1):
                        potential_password = str(pin).zfill(len(str(ending_range_value))) + first_word + second_word + third_word
                        final_wordlist.append(potential_password)
    elif where_add_number == 'end':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for third_word in third_wordlist:
                    for pin in range(starting_range_value, ending_range_value + 1):
                        potential_password = first_word + second_word + third_word + str(pin).zfill(len(str(ending_range_value)))
                        final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 3 and user_wants_add_number == 'y' and user_wants_preceeding_zeroes == 'n':
    first_wordlist = load_words(first_wordlist_location)
    second_wordlist = load_words(second_wordlist_location)
    third_wordlist = load_words(third_wordlist_location)
    if where_add_number == 'beginning':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for third_word in third_wordlist:
                    for pin in range(starting_range_value, ending_range_value + 1):
                        potential_password = str(pin) + first_word + second_word + third_word
                        final_wordlist.append(potential_password)
    elif where_add_number == 'end':
        for first_word in first_wordlist:
            for second_word in second_wordlist:
                for third_word in third_wordlist:
                    for pin in range(starting_range_value, ending_range_value + 1):
                        potential_password = first_word + second_word + third_word + str(pin)
                        final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")
elif number_of_wordlists_to_combine == 3 and user_wants_add_number == 'n':
    first_wordlist = load_words(first_wordlist_location)
    second_wordlist = load_words(second_wordlist_location)
    third_wordlist = load_words(third_wordlist_location)
    for first_word in first_wordlist:
        for second_word in second_wordlist:
            for third_word in third_wordlist:
                potential_password = first_word + second_word + third_word
                final_wordlist.append(potential_password)
    for first_word in first_wordlist:
        for second_word in second_wordlist:
            for third_word in third_wordlist:
                potential_password = first_word + second_word + third_word
                final_wordlist.append(potential_password)
    print("\nGenerating your wordlist now...")



# This block of code accomplishes the same output as the above block of code. 
# This was completed with the assistance of several people from the Central
# Ohio Python Meet-Up group. I will be using it to refactor the above block.
# if number_of_wordlists_to_combine == 1 and user_wants_add_number == 'y':
#     first_wordlist = load_words(first_wordlist_location)
#     pin_at_end = ''
#     pin_at_front = ''
#     for word in first_wordlist:
#         for pin in range(starting_range_value, ending_range_value + 1):
#             (pin_at_end := str(pin)) if where_add_number == 'end' else (pin_at_front := str(pin))
#             potential_password = f"{pin_at_front}{word}{pin_at_end}"
#             final_wordlist.append(potential_password)



# If an argument is passed on the commandline, it becomes the filename to which the wordlist is printed out.
# If no argument is given, the output is printed to 'outfile.txt' by default.
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = "outfile.txt"

with open(filename, "w") as possible_password_file:
    # print(final_wordlist, file=password_file)
    # for word in final_wordlist:
    #     print(word, file=password_file)
    my_final_copy_of_wordlist = [print(word, file=possible_password_file) for word in final_wordlist]

print(f"\nYour wordlist has been generated!")
print(f"Thank you for using WordListGen :)")


# first_wordlist = load_words(first_wordlist_location)
# print(*first_wordlist, sep="\n")
# second_wordlist = load_words(second_wordlist_location)
# third_wordlist = load_words(third_wordlist_location)
# is_valid_input = False

