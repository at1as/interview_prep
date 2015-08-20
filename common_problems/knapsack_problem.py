class KnapsackSolver(object):
  def __init__(self):
    pass

  def weights(self, weight_per_value, weight_limit, item, current_weight=0, current_value=0, items=None):
    global results_stack
 
    if items is None: 
      items = []

    current_weight += item[1]
    current_value += item[0]

    if not current_weight > weight_limit:
      results_stack.append({'weight': current_weight, 'value': current_value, 'item_list': items + [item]})
      
      new_list = items + [item]

      """
      For improved speed:
      Should check for uniqueness of entries. If for example, the results stack already has the entry [[1, 2], [2, 1]]
      And weights is called with the arguments items=[2, 1] it should not recurse through with an item argument of [1, 2]
      Since [[2, 1], [1, 2]] and [[1, 2], [2, 1]] are equivalent

      This almost does it:
        set_uniqueness = any(all(current_item in d['item_list'] for current_item in new_list) for d in results_stack)

      However, it will not correctly count for the right number of instances of a repeated entry in the list.
      Sets cannot be used either, for this reason

      """

      for w in weight_per_value:
        self.weights(weight_per_value, weight_limit, w, current_weight, current_value, items + [item])


if __name__ == "__main__":

  # Stored as [ price ($), weight (kg) ]
  weight_values = [ [4, 12], [2, 2], [2, 1], [1, 1], [10, 4] ]
  carrying_capacity = 15

  # For intensive operations these can be threaded to run simultaneously
  k = [ KnapsackSolver() ]*len(weight_values)

  print "Using the following price-weight pairs: ", [ x for x in weight_values ]
  
  for idx, x in enumerate(weight_values):
    results_stack = []

    res = k[idx].weights(weight_values, carrying_capacity, weight_values[idx])
    print "Max value starting with %s => $%s" %(weight_values[idx], max(map(lambda e: e['value'], results_stack)))


  # OUTPUT:
    # Max value starting with [4, 12] => 10
    # Max value starting with [2, 2]  => 34
    # Max value starting with [2, 1]  => 36
    # Max value starting with [1, 1]  => 35
    # Max value starting with [10, 4] => 36

