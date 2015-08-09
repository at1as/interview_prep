def radix_sort(unsorted_list, depth = 0):
  lsb = []
  valid = 0

  for item in unsorted_list:
    try:
      if depth == 0:
        lsb.append(int(str(item)[-1:]))
        valid += 1
      else:
        lsb.append(int(str(item)[(-1*depth - 1):(-1*depth)]))
        valid += 1
    except:
      lsb.append(0)
  
  if lsb[0] == 0 and len(set(lsb)) == 1:
    return unsorted_list

  # BEGIN Counting Sort
  # Cannot call counting_sort.py directly because it will not return the delta, only the rearranged LSB
  index = [x for x in range(0, 10)]
  count = [0 for x in range(0, 10)]
  
  for value in lsb:
    count[value] += 1
  
  current_sum = 0
  for idx, value in enumerate(count):
    current_sum += value
    count[idx] = current_sum
  
  sorted_list = []
  current_count = 0
  for idx, running_total in enumerate(count):
    if current_count < running_total:
      delta = running_total - current_count
      if depth == 0:
        sorted_list += [x for x in unsorted_list if int(str(x)[(-1):]) == idx]
      elif idx == 0:
        sorted_list += [x for x in unsorted_list if len(str(x)) - 1 < depth or int(str(x)[(-1*depth -1):][0]) == idx]
      else:
        sorted_list += [x for x in unsorted_list if len(str(x)) - 1 >= depth and int(str(x)[(-1*depth - 1):][0]) == idx]
      current_count += 1
  
  return radix_sort(sorted_list, depth + 1)