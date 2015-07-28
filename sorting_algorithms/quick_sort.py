def quicksort(unsorted_list, left=0, right=None):
  if right is None:
    right = len(unsorted_list) - 1

  pivot_idx = (left + right)/2 + 1
  pivot_idx = left
  right_idx = right
  left_idx = left

  while left_idx < right_idx:
    while unsorted_list[left_idx] < unsorted_list[pivot_idx]:
      left_idx += 1
    while unsorted_list[right_idx] > unsorted_list[pivot_idx]:
      right_idx -= 1

    if left_idx <= right_idx:
      left_placeholder = unsorted_list[left_idx]
      unsorted_list[left_idx] = unsorted_list[right_idx]
      unsorted_list[right_idx] = left_placeholder
      left_idx += 1
      right_idx -= 1
    
  if left < right_idx:
    unsorted_list = quicksort(unsorted_list, left, right_idx)
  if right > left_idx:
    unsorted_list = quicksort(unsorted_list, left_idx, right)

  return unsorted_list
