def selection_sort(unsorted_list):
  
  for position in range(0, len(unsorted_list)):
    pivot_value = unsorted_list[position]
    min_value = unsorted_list[position]
    min_index = position
    changed = False

    for index, value in enumerate(unsorted_list):
      if index > position:
        if value < min_value:
          min_value = value
          min_index = index
          changed = True
    
    if changed:
      unsorted_list[position] = min_value
      unsorted_list[min_index] = pivot_value

  return unsorted_list