class PriorityQueue(object):
  def __init__(self, limit=None):
    self.entries = []
    if limit is None:
      self.limit = 10
    else:
      self.limit = limit

  def saved_entries(self):
    # Return number of entries in cache
    return len(self.entries)

  def add_to_queue(self, item):
    # Add new distance to queue if it is closer than the further point in the queue
    # Assume no points are repeated

    if self.saved_entries() < self.limit:
      self.entries.append(item)
    else:
      # Assumes self.entries is sorted after every addition (and last entry is furthest)
      if self.entries[-1:][0] > item[0]:
        self.entries.pop()
        self.entries.append(item)
        self.re_sort()

  def get_closest(self):
    # Print all entries in the priority queue
    for entry in self.entries:
      print "The point (%s, %s) is a magnitude of %s away from origin" %(entry[1]['x'], entry[1]['y'], entry[0])

  def re_sort(self):
    # Re-sort 2D array in ascending order of each first column from each array 
    sorted_entries = sorted(self.entries, key=lambda x: x[0])
    self.entries = sorted_entries



def distance(source, destination):
  # Passed as (x1, y1), (x2, y2)
  # Assuming distance is on a 2D plain. On a sphere these equations are an approximation
  x_delta = destination['x'] - source['x']
  y_delta = destination['y'] - source['y']

  return math.sqrt((x_delta ** 2) + (y_delta ** 2))

def check_next_hotel(q, source, new_point):
  distance_to_hotel = distance(source, new_point)
  q.add_to_queue([distance_to_hotel, {'x': new_point['x'], 'y': new_point['y']}]) #(new_point['x'], new_point['y'])



if __name__ == "__main__":
  import math

  # See: http://www.careercup.com/question?id=5714949223481344

  q = PriorityQueue(10)

  source = {'x': 1, 'y': 1}
  points = []

  for x in range(10, 0, -1):
    for y in range(10, 0, -1):
      points.append({'x': x, 'y': y})

  for p in points:
    check_next_hotel(q, source, p)


  print "SOURCE:"
  print source

  print "HOTELS:"
  print points
  print "CLOSEST NODES:"
  print q.get_closest()


