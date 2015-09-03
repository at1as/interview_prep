def fibonacci_lsd(index1, index2, count, limit):

  if count == limit: return

  print [str(index1)[-1:], str(index2)[-1:]]

  index3 = index1 + index2

  return fibonacci_lsd(index2, index3, count + 1, limit)


if __name__ == "__main__":
  # Sum fibonacci digits and return an interval of the least signficat figures
  # [1, 1], [1, 2], [2, 3], etc...
  # http://www.careercup.com/question?id=5081134645903360
  fibonacci_lsd(1, 1, 0, 20)
