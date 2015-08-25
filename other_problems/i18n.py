# http://www.careercup.com/question?id=5733696185303040

def internalization(word):
  for x in range(len(word) - 2, -1, -1):
    for y in range(1, len(word) - 1 - x):
      print word[0:y] + str(x + 1) + word[y+x+1:]


if __name__ == "__main__":

  word = "helloworld"
  print internalization(word)