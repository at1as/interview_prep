# http://www.careercup.com/question?id=5759440689037312

def print_binary_wildcard(input_string, start_index=0):
  for i in range(start_index, len(input_string)):

    if input_string[i] == '?':
      str1 = input_string[0:i] + '0' + input_string[i+1:]
      str2 = input_string[0:i] + '1' + input_string[i+1:]
      return [print_binary_wildcard(str1, i), print_binary_wildcard(str2, i)]

  print input_string


if __name__ == "__main__":

  print '\n'
  print_binary_wildcard("?1011?010??")
  print '\n'
