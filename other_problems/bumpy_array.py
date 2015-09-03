def create_bumpy_array(array):

  # O(nlogn)
  array = sorted(array)

  even_nums = len(array) / 2

  small_values = array[:even_nums + 1]
  big_values = array[even_nums + 1:]

  return_array = []

  # O(n)
  while len(small_values) != 0:
    return_array += [small_values.pop(0)]

    if len(big_values) > 0:
      return_array += [big_values.pop(0)]

  return return_array


if __name__ == "__main__":

  # http://www.careercup.com/question?id=5681702473039872
  # Create array in which every other digit is larger than its direct left and right neighbors

  print create_bumpy_array([1, 9, 8, 6, 5, 2, 3, 4, 7])
  