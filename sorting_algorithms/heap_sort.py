def heapsort(unsorted_list):
  
  length = len(unsorted_list)
  partition = (length - 2) / 2

  # Build Heap [partition:0]
  # Each level gaurenteed to be smaller than items on parent level, but not sorted
  for x in range(partition, -1, -1):
    unsorted_list = siftdown(unsorted_list, x, length - 1)

  # Sort Heap [end:1]
  # Return fully sorted tree
  for x in range(length - 1, 0, -1):
    unsorted_list[x], unsorted_list[0] = unsorted_list[0], unsorted_list[x]
    unsorted_list = siftdown(unsorted_list, 0, x - 1)

  return unsorted_list

def siftdown(unsorted_list, begin, end):

  root = begin

  while True:
    child = (root * 2) + 1

    if child > end:
      break
    if child + 1 < end and unsorted_list[child] < unsorted_list[child + 1]:
      child += 1
    if unsorted_list[child] > unsorted_list[root]:
      unsorted_list[child], unsorted_list[root] = unsorted_list[root], unsorted_list[child]
      root = child
    else:
      break

  return unsorted_list
