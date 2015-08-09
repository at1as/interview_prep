from insertion_sort import *
from bubble_sort import *
from selection_sort import *
from bucket_sort import *
from counting_sort import *
from quick_sort import *
from merge_sort import *
from radix_sort import *
from heap_sort import *


if __name__ == "__main__":

  buckets = 3

  all_lists = {}
  all_lists['ALREADY_SORTED'] = [1, 2, 4, 4, 6, 6, 8, 9]
  all_lists['REVERSE_SORTED'] = [9, 8, 6, 6, 4, 4, 2, 1]
  all_lists['FEW_UNIQUE'] = [3, 6, 6, 4, 3, 3, 3, 6, 6, 4]
  all_lists['RANDOM_ORDER'] = [2, 6, 4, 8, 1, 4, 6, 9]
  all_lists['BIG_RANGE'] = [170, 45, 75, 90, 802, 2, 24, 66]
  all_lists['LONG_LIST'] = [2,4,3,3,6,7,876,2,4,8,214,7,2,7,4,8,2,7,4,6,83,2,6,7,88,75,2,3,6,789,86,3,6,6,3,575,6,87,8,574]
  all_lists['ZEROES_IN_LIST'] = [9,0,3,0,54,6,1,45,1,57,1,56,8,8,3,0]
  all_lists['ALL_SAME_NUMBER'] = [7,7,7,7,7,7,7,7,7,7,7]


  for list_name, number_list in all_lists.iteritems():
    print "\nUSING LIST \n\t%s\n\t%s" %(list_name, number_list)
    
    print "Insertion sorted output: \n\t", insertion_sort(number_list)
    print "Bubble sorted output: \n\t", bubble_sort(number_list)
    print "Selection sorted output: \n\t", selection_sort(number_list)
    print "Bucket sorted output (using insertion sort and %s buckets): \n\t" %(buckets), bucket_sort(number_list, 3)
    print "Counting sorted output: \n\t", counting_sort(number_list)
    print "Quick sorted output: \n\t", quicksort(number_list)
    print "Merge sorted output: \n\t", mergesort(number_list)
    print "Radix sorted output (using counting sort): \n\t", radix_sort(number_list)
    print "Heap sorted output: \n\t", heapsort(number_list)
    