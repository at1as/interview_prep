def get_horizontal_distance(floor_map, row, column, size=5):
  # Return nearest distance to guard along vertical path. Return 'inf' if none
  right = float('inf')
  left = float('inf')


  # Distance to guard (towards the left)
  for x in range(0, column):
    if floor_map[row][x] == 'G':
      left = column - x
    elif floor_map[row][x] == '#':
      left = float('inf')

  # Distance to guard (towards the right)
  for x in range(column + 1, size):
    if floor_map[row][x] == 'G':
      right = x - column
      break
    elif floor_map[row][x] == '#':
      break
  
  return min(left, right)


def get_vertical_distance(floor_map, row, column, size=4):
  # Return nearest distance to guard along vertical path. Return 'inf' if none
  top = float('inf')
  bottom = float('inf')


  # Distance to guard (upwards)
  for y in range(0, row):
    if floor_map[y][column] == 'G':
      top = row - y
    elif floor_map[y][column] == '#':
      top = float('inf')

  # Distance to guard (downwards)
  for y in range(row + 1, size):
    if floor_map[y][column] == 'G':
      bottom = y - row
      break
    elif floor_map[y][column] == '#':
      break

  return min(top, bottom)


def get_neighbor_distance(floor_map, row, column, xlim=5, ylim=4):
  # Will check for path from neighbor to guard, but this function should be recursive to ensure a solution
  if column == xlim - 1:
    right = None
  else:
    right = min(get_vertical_distance(floor_map, row, column + 1), get_horizontal_distance(floor_map, row, column + 1))

  if column == 0:
    left = None
  else:
    left = min(get_vertical_distance(floor_map, row, column - 1), get_horizontal_distance(floor_map, row, column - 1))

  if row == ylim - 1:
    bottom = None
  else:
    bottom = min(get_vertical_distance(floor_map, row + 1, column), get_horizontal_distance(floor_map, row + 1, column))
  
  if row == 0:
    top = None
  else:
    top = min(get_vertical_distance(floor_map, row - 1, column), get_horizontal_distance(floor_map, row - 1, column))

  return 1 + min(filter(lambda x: x is not None, [top, bottom, left, right]))


def distance_to_guard(floor_map):
  # Find minimum distance in the floor_map from point '.' to a guard 'G'
  # Only lateral movements are permitted, and currently only direct neighbors are traversed for multi-direction paths

  for row_idx in range(0, len(floor_map)):
    for col_idx in range(0, len(floor_map[0])):

      if floor_map[row_idx][col_idx] != '#' and floor_map[row_idx][col_idx] != 'G':
        dist = min(get_horizontal_distance(floor_map, row_idx, col_idx), get_vertical_distance(floor_map, row_idx, col_idx), get_neighbor_distance(floor_map, row_idx, col_idx))
        floor_map[row_idx][col_idx] = dist


if __name__ == "__main__":
  # http://www.careercup.com/question?id=5630807089610752

  floor_map = [
                [ '.', '#', '.', 'G', '.'],
                [ '.', '.', '#', '.', '.'],
                [ 'G', '.', '.', '.', '.'],
                [ '.', '.', '#', '.', '.']
              ]

  distance_to_guard(floor_map)

  for r in floor_map:
    print r
