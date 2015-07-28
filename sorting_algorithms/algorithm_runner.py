from insertion_sort import *
from bubble_sort import *
from selection_sort import *
from bucket_sort import *
from counting_sort import *
from quick_sort import *

# merge_sort, heapsort, radix_sort

if __name__ == "__main__":

  buckets = 3

  ALREADY_SORTED = [1, 2, 4, 4, 6, 6, 8, 9]
  REVERSE_SORTED = [9, 8, 6, 6, 4, 4, 2, 1]
  FEW_UNIQUE = [3, 6, 6, 4, 3, 3, 3, 6, 6, 4]
  RANDOM_ORDER = [2, 6, 4, 8, 1, 4, 6, 9]
  BIG_RANGE = [170, 45, 75, 90, 802, 2, 24, 66]
  LONG_LIST = [2,4,3,3,6,7,876,2,4,8,214,7,2,7,4,8,2,7,4,6,83,2,6,7,88,75,2,3,6,789,86,3,6,6,3,575,6,87,8,574]

  all_lists = [ALREADY_SORTED, REVERSE_SORTED, FEW_UNIQUE, RANDOM_ORDER, BIG_RANGE, LONG_LIST]

  for idx, number_list in enumerate(all_lists):
    print "\nUSING LIST \n\t%s" %(all_lists[idx])

    print "Insertion sorted output: \n\t", insertion_sort(number_list)
    print "Bubble sorted output: \n\t", bubble_sort(number_list)
    print "Selection sorted output: \n\t", selection_sort(number_list)
    print "Bucket sorted output (using insertion sort and %s buckets): \n\t" %(buckets), bucket_sort(number_list, 3)
    print "Counting sorted output: \n\t", counting_sort(number_list)
    print "Quick sorted output: \n\t", quicksort(number_list)
