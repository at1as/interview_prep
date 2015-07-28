def bucket_sort(unsorted_list, total_buckets):
  from insertion_sort import *

  current_max = None
  for value in unsorted_list:
    if value > current_max: current_max = value

  # Weird way to round up an integer without needing external libraries
  bucket_bounds = int(current_max / total_buckets) + (current_max % total_buckets > 0)
  buckets = [[] for x in range(0, total_buckets)]

  for number in unsorted_list:
    if number is 0:
      buckets[0].append(number)
    else:
      buckets[((number - 1)/bucket_bounds)].append(number)
  
  sorted_list = []
  for bucket in buckets:
    sorted_list += insertion_sort(bucket)

  return sorted_list