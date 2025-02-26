import random, sys

# ask for length of password
try:
    pass_length = int(input("\nCharacter Length of Password: \n"))
    if pass_length > 50:
        sys.exit("\npassword too big\n")
except ValueError:
    sys.exit("\nYou didn't type a real number.\n")

# define password variable so it can be concatinated
password = ""
# define the range of characters to pick
char_range = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", "!", "@", "#", "$", "%", "&", "/", "?", ".")

# set i = 0
i = 0
# while loop to add characters to password until its the chosen length
while i < pass_length:
    password = password + random.choice(char_range)
    i += 1

# say password and exit
sys.exit(f"\nYour password is: {password}\n")