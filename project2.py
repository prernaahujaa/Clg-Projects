import random
import array

# maximum length of password needed
MAX_LEN = 12

# declare arrays of the characters need in generating password
# Represented as chars to enable string concatenation
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LCASE_ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UCASE_ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']

# combined all the character arrays above to form one array
COMBINED_LIST = DIGITS + UCASE_ALPHABETS + LCASE_ALPHABETS + SYMBOLS

# randomly select at least one character from each set above
rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UCASE_ALPHABETS)
rand_lower = random.choice(LCASE_ALPHABETS)
rand_symbol = random.choice(SYMBOLS)

# combine the character randomly selected above
# now the password contains only 4 characters but
# we want a 12-character password
temporary_pass = rand_digit + rand_upper + rand_lower + rand_symbol


# now we are sure we have at least one character from each
# set of characters, we fill the rest of
# the password length by selecting randomly from the combined
# list of character above.
for x in range(MAX_LEN - 4):
	temporary_pass = temporary_pass + random.choice(COMBINED_LIST)

	# converted temporary password into array and shuffle to
	# prevent it from having a consistent pattern
	# where the beginning of the password is predictable
	temporary_pass_list = array.array('u', temporary_pass)
	random.shuffle(temporary_pass_list)

# traverse the temporary password array and append the chars
# to form the password
password = ""
for x in temporary_pass_list:
		password = password + x
		
# print out password
print("new password is = ", password)
