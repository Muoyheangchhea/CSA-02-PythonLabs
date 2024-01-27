
# Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
# Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes a hyphen will separate the two letters in the string.

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #write down all of the alphabet total range
userinput = input("Enter a range of letters (e.g., a-z): ") #ask user to input letter from one - another using split as "to" e.g. a-m
start, end = userinput.split("-") #analyze start and end point by getting the user input range e.g. a-m so, start=a, end=m
startnum = alphabet.index(start) #using index function to find the position of the start point e.g. a = 0
endnum = alphabet.index(end) #using index function to find the position of the end point e.g. m = 12
range = alphabet[startnum:endnum + 1] #using range alphabet[num1:num2] which means the position of num1 to num2 
#e.g. alphabet[0:12] which means in alphabet variable, it displays from letter in 0 position to 12 position
#note: variable[:] only works with number, not string and that's why we have to find the number of position in the start and end
print("The alphabets between " + start + " and " + end + " are", range)


