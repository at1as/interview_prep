# http://www.careercup.com/question?id=5067106322219008

def next_sequence(input_string):
	
	next_str = ""

	number = input_string[0]
	count = 1

	for char in input_string[1:]:
		if char == number:
			count += 1
		else:
			next_str = next_str + str(count) + str(number)
			number = char
			count = 1

	return next_str + str(count) + str(number)


if __name__ == "__main__":

	# 1 -> 11 -> 21 -> 1211 -> 111221 -> 312211 -> etc.
	# one -> one one -> two ones -> one two & one one -> one one & one two & two ones -> etc.

	print next_sequence("111221")
