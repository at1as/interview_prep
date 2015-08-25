def make_sentence(phone_number, buffer=""):
  # Turn phone number digits into all possible words those numbers can represent
  # See number_mapping below
  # This function adds all permutations to the stack
  global number_stack
  
  if len(buffer) == len(phone_number):
    for digit in number_mapping[phone_number[-1:]]:
      number_stack.append((buffer + digit))
  else:
    index = len(buffer)
    for digit in number_mapping[phone_number[index]]:
      make_sentence(phone_number, buffer + digit)


if __name__ == "__main__":
  
  number_stack = []

  number_mapping = {
    '0': ['0'],
    '1': ['1'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['K', 'L', 'M'],
    '6': ['N', 'O', 'P'],
    '7': ['Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z']
  }

  phone_number = "1234567"

  make_sentence(phone_number)

  print "Possible words: ", number_stack
