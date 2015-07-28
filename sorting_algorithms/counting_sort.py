def counting_sort(unsorted_list):
  current_max = None
  for value in unsorted_list:
    if value > current_max: current_max = value

  index = [x for x in range(0, current_max + 1)]
  count = [0 for x in range(0, current_max + 1)]

  for number in unsorted_list:
    count[number] += 1

  current_sum = 0
  for i in range(0, current_max + 1):
    current_sum += count[i]
    count[i] = current_sum

  sorted_list = []

  current_count = 0
  for i in index:
    while current_count < count[i]:
      sorted_list.append(index[i])
      current_count += 1
  
  return sorted_list