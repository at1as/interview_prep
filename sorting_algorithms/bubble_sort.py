def bubble_sort(unsorted_list):
  list_length = len(unsorted_list)
  changed = True

  while changed:
    changed = False
    for idx, val in enumerate(unsorted_list):

      if idx < list_length - 1:
        current_item = val
        next_item = unsorted_list[idx + 1]
        
        if current_item > next_item:
          unsorted_list[idx] = next_item
          unsorted_list[idx + 1] = current_item
          changed = True
  
  return unsorted_list