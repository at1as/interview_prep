
class Node(object):
  def __init__(self, name, prev=None, next=None):
    self.name = name
    self.prev = prev
    self.next = next

class LinkedList(object):
  def __init__(self, nodes=None):
    self.nodes = []

  def add_node(self, node):
    self.nodes.append(node)

  def has_node(self, node):
    for n in self.nodes:
      if n.name == node:
        return True
    return False

  def get_node(self, name):
    for n in self.nodes:
      if n.name == name:
        return n

  def get_head(self):
    n = self.nodes[0]
    while n.prev:
      n = n.prev

    return n

  def print_links(self):
    start = self.get_head()
    while start.next:
      print "%s ->" %(start.name)
      start = start.next

    print start.name


if __name__ == "__main__":
  # http://www.careercup.com/question?id=5079989210841088
  
  tickets = [ ['MUC', 'LHR'],
              ['CDG', 'MUC'],
              ['SFO', 'SJC'],
              ['LHR', 'SFO']]

  locations = LinkedList()

  for trip in tickets:
    if not locations.has_node(trip[0]):
      locations.add_node(Node(trip[0]))
    if not locations.has_node(trip[1]):
      locations.add_node(Node(trip[1]))

    locations.get_node(trip[0]).next = locations.get_node(trip[1])
    locations.get_node(trip[1]).prev = locations.get_node(trip[0])

  locations.print_links()
  