class KnapsackSolver(object):
  def __init__(self):
    pass

  def weights(self, weight_per_value, weight_limit, item, current_weight=0, current_value=0, items=None):
 
    if items is None: 
      items = []

    current_weight += item[1]
    current_value += item[0]

    if current_weight > weight_limit:
      return
    else:

      #return {'weight': current_weight, 'value': current_value, 'item_list': items + [item]}, [
      #self.weights(weight_per_value, weight_limit, i, current_weight, current_value, items + [item]) for i in weight_per_value if self.weights(weight_per_value, weight_limit, i, current_weight, current_value, items + [item]) is not None]

      return [ {'weight': current_weight, 'value': current_value, 'item_list': items + [item]} ] + [
      self.weights(weight_per_value, weight_limit, i, current_weight, current_value, items + [item]) for i in weight_per_value if self.weights(weight_per_value, weight_limit, i, current_weight, current_value, items + [item]) is not None]

      #return [{'weight': current_weight, 'value': current_value, 'item_list': items + [item]}] + filter(lambda item: self.weights(weight_per_value, weight_limit, item, current_weight, current_value, items + [item]), weight_per_value)
      #self.weights(weight_per_value, weight_limit, i, current_weight, current_value, items + [item]) for i in weight_per_value if self.weights(weight_per_value, weight_limit, i, current_weight, current_value, items + [item]) is not None]

  def unscramble_mess(self, data, max={}):

    length = len(data)

    if type(data) == type({}):
      print "D IS", data['value']
      return data['value']
    else:
      #return [self.unscramble_mess(datum) for datum in data]
      #return filter(lambda datum: self.unscramble_mess(datum), data)
      f = lambda a,b: a if (a > b) else b
      print "S", filter(lambda datum: self.unscramble_mess(datum), data)
      return reduce(f, filter(lambda datum: self.unscramble_mess(datum), data))

if __name__ == "__main__":

  from compiler.ast import flatten

  # Stored as [ price ($), weight (kg) ]
  weight_values = [ [4, 12], [2, 2], [2, 1], [1, 1], [10, 4] ]
  carrying_capacity = 15

  k = [ KnapsackSolver() ]*len(weight_values)

  for idx, x in enumerate(weight_values):
    res = k[idx].weights(weight_values, carrying_capacity, weight_values[idx])
    print "Max value starting with %s => %s" %(weight_values[idx], max(map(lambda e: e['value'], flatten(res))))


  
  

