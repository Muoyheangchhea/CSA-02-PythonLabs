
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.


alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Get user input for the letter range
user_range = input("Enter a range of letters (e.g., a-z): ")

# Extract start and end letters from the user input
start_letter, end_letter = user_range.split('-')
start_index = alphabet.index(start_letter)
end_index = alphabet.index(end_letter)

# Create the result string by slicing the alphabet
result_string = alphabet[start_index:end_index + 1]

# Convert the result string to uppercase if the start letter is uppercase

print(result_string)

