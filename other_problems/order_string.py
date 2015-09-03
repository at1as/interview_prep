def string_reorder(s, o):

  unordered_letters = []
  ordered_letters = {}

  # O(len(o))
  for letter in o: 
    ordered_letters[letter] = 0

  # O(len(s))
  for letter in s:
    if ordered_letters.has_key(letter):
      ordered_letters[letter] += 1
    else:
      unordered_letters += [letter]

  # O(len(s) - len(ordered_letters))
  for letter in o:
    unordered_letters += [letter] * ordered_letters[letter]

  return ''.join(unordered_letters)


if __name__ == "__main__":
  
  # http://www.careercup.com/question?id=5651258268450816

  print string_reorder('hello world', 'wrled')