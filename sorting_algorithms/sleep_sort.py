from multiprocessing import Process, Manager, Lock
from time import sleep

def sleepsort(array, sorted_array):
  subprocesses = []

  for value in array:
    p = Process(target=sleep_for_value, args=(value, sorted_array,))
    subprocesses.append(p)
    p.start()

  for subprocess in subprocesses:
    subprocess.join()

  return sorted_array

def sleep_for_value(n, sorted_array):
  sleep(n)
  sorted_array.append(n)
  print n   # carraige return is not thread safe


if __name__ == "__main__":
  manager = Manager()
  sorted_list = manager.list()
  unsorted_list = [3,4,5,6,7,8,5,1,1,1,2,40,5,3,7,2,9,14,6,7,1] 
  res = sleepsort(unsorted_list, sorted_list)

  print res

