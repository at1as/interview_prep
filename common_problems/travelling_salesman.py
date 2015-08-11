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
    """
      return the shortest path from `start` to `finish`
    """

    if start == finish: return sum

    next_nodes = [item for item in [v for v in start.verticies] if item not in set(visited_nodes + [start])]
    
    try:
      return min([self.shortest_path(node, finish, visited_nodes + [start], sum + start.verticies[node]) for node in next_nodes if self.shortest_path(node, finish, visited_nodes + [start], sum + start.verticies[node]) is not None])
    except:
      pass
  


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


  def minimum_spanning_tree(self, nodes, node, nodes_visited=None, sum=0):
    """
      Using Prim's Greedy algorithm, connect shortest paths until all nodes have been visited
    """
    if nodes_visited is None:
      nodes_visited = [node]
    else:
      nodes_visited.append(node)

    verticies = sorted(node.verticies.items(), key=lambda x: x[1])

    # for node, recurse to next nearest node that was not visited already, and that isn't the removed node
    for vertex in verticies:
      if vertex[0] not in nodes_visited and vertex[0] in nodes:
        return self.minimum_spanning_tree(nodes, vertex[0], nodes_visited, sum + vertex[1])

    return sum

  
  def lower_bound(self, removed_node, active_nodes):
    """
      Remove one node from graph. Calculate minimum spanning tree betwen remaining nodes
      Then add two smallest paths from the removed node to the spanning tree
    """
    spanning_distance = self.minimum_spanning_tree(active_nodes, active_nodes[0])

    # Add two shortest paths from removed nodes to the spanning tree
    connecting_distance = sum(map(lambda x: x[1], sorted(removed_node.verticies.items(), key=lambda x: x[1]))[0:2])

    return connecting_distance + spanning_distance


  def shortest_unbounded_path(self, nodes, node, visited_nodes=None, sum=0):
    if visited_nodes is None:
      visited_nodes = []

    # If all nodes have been visited, return current sum and the magnitude of the path back to the starting point
    if set(visited_nodes + [node]) == set(nodes):
      return_path = self.shortest_path(node, visited_nodes[0])
      print "%s : %s via path %s with return distance of %s" %(sum + return_path, sum, [x.name for x in visited_nodes + [node]], return_path)

    verticies = node.verticies
    unique_verticies = []

    # Visit all node verticies that have not yet been visited
    for vertex in verticies:
      if vertex not in set(visited_nodes + [node]):
        unique_verticies += [vertex]

    for vertex in unique_verticies:
      self.shortest_unbounded_path(nodes, vertex, visited_nodes + [node], sum + verticies[vertex])


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

  print "Upper Bound:", g.upper_bound(a)
  print "Lower Bound:", g.lower_bound(c, [a, b, d, e])
  
  print "Shortest Path from A:"
  g.shortest_unbounded_path([a, b, c, d, e], a)
  print "Shortest Path from B:"
  g.shortest_unbounded_path([a, b, c, d, e], b)
  print "Shortest Path from C:"
  g.shortest_unbounded_path([a, b, c, d, e], c)
  print "Shortest Path from D:"
  g.shortest_unbounded_path([a, b, c, d, e], d)
  print "Shortest Path from E:"
  g.shortest_unbounded_path([a, b, c, d, e], e)

