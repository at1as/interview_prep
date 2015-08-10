class Node(object):
  def __init__(self, name, verticies=None):
    self.name = name
    if verticies is None:
      self.verticies = {}
    else:
      self.verticies = verticies

  def name(self):
    return self.name

  def verticies(self):
    return self.verticies

  def add_vertex(self, n, distance):
    self.verticies[n] = distance

  def add_verticies(self, dict_of_verticies):
    for vertex in dict_of_verticies:
      self.add_vertex(vertex, dict_of_verticies[vertex])

  def distance_to(self, name):
    for vertex in self.verticies:
      if vertex.name == name:
        return vertex.name


class Graph(object):
  def __init__(self, node_list = []):
    self.nodes = node_list

  def nearest_neighbors(self, node):
    return sorted(node.verticies.items(), key=lambda x: x[1])

  def nearest_unique(self, sorted_neighbors, visited_nodes):
    for idx, neighbor in enumerate(sorted_neighbors):
      if sorted_neighbors[idx][0] not in visited_nodes:
        return sorted_neighbors[idx][0]
    return None 


  def shortest_path(self, start, finish, visited_nodes=[], sum=0):

    if start == finish: return sum

    visited_nodes.append(start)
    next_nodes = [item for item in [v for v in start.verticies] if item not in visited_nodes]
    
    return min([self.shortest_path(node, finish, visited_nodes, sum + start.verticies[node]) for node in next_nodes])
    

  def upper_bound(self, start, current=None, visited_nodes=[], sum=0):
    """
    Start with a given node, and calculate nearest neightbor recursively until all nodes have been touched.
    Once they've all been touched, calculate shortest path from the last node to the original one
    """

    if current is None: current = start
    visited_nodes.append(current)

    next_node = self.nearest_unique(self.nearest_neighbors(current), visited_nodes)

    if next_node is None:
      return sum + self.shortest_path(start, current)

    return self.upper_bound(start, next_node, visited_nodes, sum + current.verticies[next_node])


  def lower_bound(self, removed_node, active_nodes, sum):
    """
      Remove one node from graph. Calculate minimum spanning tree betwen remaining nodes
      Then add two smallest paths from the removed node to the spanning tree
      JW: TODO
    """
    pass


if __name__ == "__main__":
  """
      B
    / | \
   A -E- C
    \ | /
      D
  """
  a = Node('A')
  b = Node('B')
  c = Node('C')
  d = Node('D')
  e = Node('E')
  a.add_verticies({b: 16, e: 22, d: 14})
  b.add_verticies({a: 16, e: 4, c: 18})
  c.add_verticies({b: 18, e: 23, d: 19})
  d.add_verticies({a: 14, e: 7, c: 19})
  e.add_verticies({a: 22, b: 4, c: 23, d: 7})

  g = Graph([a, b, c, d, e])

  print g.upper_bound(a)
  #print g.lower_bound(c, [a, b, d, e])

