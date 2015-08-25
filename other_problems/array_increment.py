# Question: http://www.careercup.com/question?id=4809209524781056

def increment(array, index=None, carry=False):

  if index is None:
    index = len(array) - 1

  if carry and index == 0:
    if int(array[index]) < 9:
      return [array[0] + 1] + array[1:]
    else:
      return [1, 0] + array[1:]

  if int(array[index]) < 9:
    return array[:index] + [int(array[index]) + 1] + array[index + 1:]
  elif int(array[index]) == 9:
    new_array = array[:index] + [0] + array[index + 1:]
    return increment(new_array, index - 1, True)


if __name__ == "__main__":
  a1 = [1,2,3]
  a2 = [9,1,7]
  a3 = [9,9,9]
  a4 = [9]
  a5 = [0]
  a6 = [0, 9]
  a7 = [1, 9, 0, 0]
  a8 = [2, 7, 9]
  a9 = [2, 9, 3]
  a10 = [9, 8, 9, 9]
  a11 = [1, 9, 4]
  a12 = [1, 9]

  for idx, lst in enumerate([a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]):
    print "Array %s was %s and is now %s" %(idx, lst, increment(lst))

