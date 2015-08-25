def print_spiral(array):
  # Spiral around a 2D array printing each entry

  top = 0
  left = 0
  bottom = len(array) - 1
  right = len(array[0]) - 1

  direction = 0

  while top < bottom or left < right:
    if direction == 0:
      for i in range(left, right + 1):
        print array[top][i]
      
      top += 1
      direction = 1
    elif direction == 1:
      for i in range(top, bottom + 1):
        print array[i][right]

      right -= 1
      direction = 2
    elif direction == 2:
      for i in range(right, left - 1, -1):
        print array[bottom][i]

      bottom -= 1
      direction = 3
    elif direction == 3:
      for i in range(bottom, top - 1, -1):
        print array[i][left]

      left += 1
      direction = 0      



if __name__ == "__main__":

  array = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
        ]

  for a in array:
    print a

  print_spiral(array)