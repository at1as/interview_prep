# http://www.careercup.com/question?id=6303093824159744

def canoe(array, canoe_count=0):
  # Return number of canoes necessary to hold a group of children
  # If each canoe can hold up to 150 kg and a maximum of two children

  array_length = len(array)

  # No children left. Return current number of canoes
  if array_length == 0:
    return canoe_count

  # Only one child left. Return current number of canoes + one extra for remaining child
  if array_length == 1:
    print "> Adding last child %s to one canoe" %(array[0])
    return canoe_count + 1

  # Put only one child in a canoe if:
  #   - The heaviest child uses all of the canoe weight allowance
  #   - The heaviest and lightest child together would exceed the weight allowance
  elif array[-1:][0] >= 150 or array[-1:][0] + array[0] > 150:
    print "> Adding %s to one canoe" %(array[-1:][0])
    print "Children remaining %s" %(array[0:-1])

    return canoe(array[0:-1], canoe_count + 1)

  else:
    # Pair the heaviest child with the lightest child
    # If the max weight is not exceeded, take the second lightest lightest child, etc
    # Until max weight is exceeded
    heaviest = array[-1:][0]
    lightest = array[0]

    count = 0
    while count < array_length - 2:
      if heaviest + array[count + 1] < 150:
        count += 1
        lightest = array[count]
      else:
        break
      
    # Remove the lighter child from the array
    l = array.pop(count)
    h = array[-1:][0]
    
    print "> Adding %s and %s to one canoe" %(l,h)
    print "Children remaining %s" %(array[:-1])

    return canoe(array[:-1], canoe_count + 1)

  

if __name__ == "__main__":
  
  weights = [70, 75, 100, 150, 60, 80, 45]
  weights = sorted(weights)

  print "Input: %s" %(weights)
  print "\nCanoes necessary: %s \n" %(canoe(weights))
