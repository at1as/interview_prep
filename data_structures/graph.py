class Node(object):
  def __init__(self, name, arcs):
    self.name = name
    self.arcs = arcs

  def arcs(self):
    return self.arcs

  def add_arc(self, arc):
    self.arcs.append(arc)

  def remove_arc(self, arc):
    for idx, existing_arc in enumerate(self.arcs):
      if arc.lower() == existing_arc.lower():
        self.arcs.pop(idx)


class Graph(object):
  def __init__(self, node_list):
    self.node_list = node_list

  def add_node(self, node):
    # Add new node to graph
    self.node_list.append(node)

  def delete_node(self, node_name):
    # Remove ndoe from node_list. Remove all arcs to that node
    for idx1, node in enumerate(self.node_list):
      if node.name.lower() == node_name.lower():
        self.node_list.pop(idx1)
      if node_name.lower() in [arc.lower() for arc in node.arcs]:
        node.remove_arc(node_named)

  def _get_node(self, node_name):
    # Return node from node_name
    for node in self.node_list:
      if node.name.lower() == node_name.lower():
        return node

  def _node_in_path(self, node, path):
    # Return true if node is in path, else false
    for path_node_name in path:
      if path_node_name.lower() == node.lower():
        return True
    return False

  def print_graph(self):
    # Print each node name and all arcs for each node
    for node in self.node_list:
      print "%s => %s" %(node.name, node.arcs)

  def direct_pointer_to(self, node):
    # print all node names that point to 'node'
    pointers = []
    for path_node in self.node_list:
      if node.name.lower() in [arc.lower() for arc in path_node.arcs]:
        pointers.append(path_node.name)
    return pointers

  def path_between(self, start, end, path=[]):
    path = path + [start.name]

    if not start in self.node_list:
      return None
    if start == end:
      return path
    for arc in start.arcs:
      if not self._node_in_path(arc, path):
        new_path = self.path_between(self._get_node(arc), end, path)
        if new_path:
          return new_path
    return None

  def shortest_path(self, start, end, path=[], results=[]):
    path.append(start)

    if not start in self.node_list:
      return None
    if start == end:
      return None
    for arc in start.arcs:
      #if arc not in path:
      if not self._node_in_path(arc, path):
        new_path = self.paths_between(arc, end, path)
        if new_path:
          results.append(new_path)
    return results
