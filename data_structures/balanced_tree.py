"""
Usage:
  from balanced_tree import *
  a = Node(3); b = Node(4); c = Node(5); d = Node(6); e = Node(7); f = Node(8)
  a.left = b; a.right = c; c.left = d; c.right = f; d.left = e; 
  t = Tree(a)
  t.tree_sum(); t.tree_nodes()
"""

class Node(object):
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

  def value(self): 
    return self.value
  
  def left(self): 
    return self.left
  
  def right(self): 
    return self.right

  def value(self, value):
    self.value = value

  def left(self, left):
    self.left = left

  def right(self, right):
    self.right = right


class Tree(object):
  def __init__(self, root):
    self.root = root
    self.nodes = []

  def tree_levels(self, n, level = 0):
    # Return max depth of the tree
    if n is None:
      return level

    return max(self.tree_levels(n.left), self.tree_levels(n.right)) + 1

  def tree_nodes(self, n = None, count = None):
    # Return number of nodes on the tree
    if count is None:
      count = 1

    if n is None:
      n = self.root

    if n.left and n.right:
      return count + self.tree_nodes(n.left, count) + self.tree_nodes(n.right, count)
    elif n.left:
      return count + self.tree_nodes(n.left, count)
    elif n.right:
      return count + self.tree_nodes(n.right, count)
    if not n.left and not n.right:
      return count

  def tree_sum(self, n = None, sum = None):
    # Return sum of all nodes in the tree
    if sum is None: 
      sum = 0
    if n is None: 
      n = self.root

    if n.left and n.right:
      return n.value + self.tree_sum(n.left, sum) + self.tree_sum(n.right, sum)
    elif n.left:
      return n.value + self.tree_sum(n.left, sum)
    elif n.right:
      return n.value + self.tree_sum(n.right, sum)
    if not n.left and not n.right:
      return n.value

  def tree_sum_at_level(self, desired_level = 0, n = None, current_level = 0):
    # Return sum of all nodes at desired_level of tree
    if n is None:
      n = self.root

    if current_level > desired_level:
      return 0
    elif current_level < desired_level:
      offset = 0
    elif current_level == desired_level:
      offset = n.value

    if n.left and n.right:
      return offset + self.tree_sum_at_level(n.left, desired_level, current_level + 1) + self.tree_sum_at_level(n.right, desired_level, current_level + 1)
    elif n.left:
      return offset + self.tree_sum_at_level(n.left, desired_level, current_level + 1)
    elif n.right:
      return offset + self.tree_sum_at_level(n.right, desired_level, current_level + 1)
    if not n.left and not n.right:
      return offset

  def balanced(self):
    # If the tree is balanced (that is, if the tree has minimum possible depth for given nodes)
    node_count = self.tree_nodes(self.root)
    depth = self.tree_levels(self.root)

    max_allowed = (2 ** (depth + 1)) - 1
    if max_allowed > node_count:
      return False
    else:
      return True

  def get_nodes(self):
    return self.nodes

  def search_level_order(self, n=None):
    # Bredth first search
    if n is None:
      n = self.root
      self.nodes.append(n)

    if n.left:
      self.nodes.append(n.left)
    if n.right:
      self.nodes.append(n.right)

    if n.left:
      self.search_level_order(n.left)
    if n.right:
      self.search_level_order(n.right)

  def pre_order(self, n=None):
    # Depth first search (Root, Left, Right)
    if n is None:
      n = self.root
      self.nodes = []
    
    print n.value
    self.nodes.append(n)

    if n.left:
      self.pre_order(n.left)
    if n.right:
      self.pre_order(n.right)

  def in_order(self, n=None):
    # Depth first search (Left, Root, Right)

    if n is None:
      n = self.root

    if n.left:
      self.in_order(n.left)
    print n.value
    if n.right: 
      self.in_order(n.right)

  def post_order(self, n=None):
    # Depth first search (Left, Right, Root)

    if n is None:
      n = self.root

    if n.left: 
      self.post_order(n.left)
    if n.right: 
      self.post_order(n.right)
    print n.value
