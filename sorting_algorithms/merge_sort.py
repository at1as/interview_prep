def mergesort(unsorted_list):
  if len(unsorted_list) > 1:
    
    mid = len(unsorted_list) / 2
    left_side, right_side = unsorted_list[:mid], unsorted_list[mid:]
    
    # Recursively apply mergesort to each side
    mergesort(left_side)
    mergesort(right_side)

    left_idx, right_idx, count = 0, 0, 0

    while left_idx < len(left_side) and right_idx < len(right_side):
      if left_side[left_idx] < right_side[right_idx]:
        unsorted_list[count] = left_side[left_idx]
        left_idx += 1
      else:
        unsorted_list[count] = right_side[right_idx]
        right_idx += 1
      count += 1

    while left_idx < len(left_side):
      unsorted_list[count] = left_side[left_idx]
      left_idx += 1
      count += 1

    while right_idx  > len(right_side):
      unsorted_list[count] = right_side[right_idx]
      right_idx += 1
      count += 1

  return unsorted_list