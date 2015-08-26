def fancy_shuffle(input_string):
  characters = {}
  for char in input_string:
    if characters.has_key(char):
      characters[char] += 1
    else:
      characters[char] = 1

  # Create a 2D array of size equal to letter that occurs the most frequently in the string
  # Ex. "AAABBCC" -> [[A], [A], [A]]
  largest_key = max(characters, key=lambda x: characters[x])
  largest_val = characters[largest_key]
  groups = [[largest_key] for i in range(0, largest_val)]

  # most frequently occuring character has already been distributed into the 2D groups array 
  characters[largest_key] = 0
  
  # Break loop when no more changes are made
  change_made = True
  idx = 0

  # There must be enough letters to interleave with, or characters will repeat in value
  if sum(map(lambda x: characters[x], characters)) < largest_val:
    return -1

  # Append remaining letters to each array within groups (at index idx), one at a time
  while change_made:
    change_made = False

    for c in characters:
      if characters[c] >= 1:
        groups[idx] += c
        characters[c] -= 1
        idx = (idx + 1) % largest_val
        change_made = True

  # Return 2D array as a string
  # Ex. [['a', 'b', 'c'], ['a', 'b']] -> 'abcab'
  return "".join(["".join(g) for g in groups])


if __name__ == "__main__":

  # http://www.careercup.com/question?id=5631166847647744
  print "Input: \n\t%s" %('AAAAAAAAABBBBCCDDDDDEFFFF')
  print "Output:\n\t%s" %(fancy_shuffle("AAAAAAAAABBBBCCDDDDDEFFFF"))
