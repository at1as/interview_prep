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

  def add_to_tree(self, new_node, current_node=None):
    # Add node to tree in appropriate place
    if current_node is None:
      current_node = self.root

    if new_node.value > current_node.value:
      if current_node.right is None:
        current_node.right = new_node
      else:
        self.add_to_tree(new_node, current_node.right)

    elif new_node.value < current_node.value:
      if current_node.left is None:
        current_node.left = new_node
      else:
        self.add_to_tree(new_node, current_node.left)


  def is_bst(self, current_node=None):
    # Return 1 if BST condition satisified, else 0
    if current_node is None:
      current_node = self.root

    # Check if each child exists, and if the left child is smaller and right child larger than parent
    if (current_node.left is not None and current_node.left.value < current_node.value) and (current_node.right is not None and current_node.right > current_node.value):
      return self.is_bst(current_node.left) * self.is_bst(current_node.right)

    elif current_node.left is not None and current_node.left.value < current_node.value:
      return self.is_bst(current_node.left)
    
    elif current_node.right is not None and current_node.right.value > current_node.value:
      return self.is_bst(current_node.right)
    
    elif current_node.left is None and current_node.right is None:
      return True

    else:
      return False


  def remove_node(self, value_to_remove, current_node=None, parent_node=None, direction=None):
    # Remove a node from BST and preserve connections between other nodes
    # See three cases below for node selected for removal
    if current_node is None:
      current_node = self.root

    if current_node.value < value_to_remove:
      self.remove_node(value_to_remove, current_node.right, current_node, "right")
    elif current_node.value > value_to_remove:
      self.remove_node(value_to_remove, current_node.left, current_node, "left")
    else:

      # Case 1: No children
      if current_node.left is None and current_node.right is None:
        if direction == "right":
          parent_node.right = None
        elif direction == "left":
          parent_node.left = None

      # Case 2: One Child
      elif current_node.right is None:
        if direction == "right":
          parent_node.right = current_node.left
        elif direction == "left":
          parent_node.left = current_node.left

      elif current_node.left is None:
        if direction == "right":
          parent_node.right = current_node.right
        elif direction == "left":
          parent_node.left = current_node.right

      # Case 3: Two Children
      else:
        left_tree_max, left_tree_root = self.pop_max(current_node.left)

        if direction == "right":
          parent_node.right = left_tree_max
        elif direction == "left":
          parent_node.left = left_tree_max

        left_tree_max.right = current_node.right
        left_tree_max.left = left_tree_root


  def pop_max(self, current_node, parent_node=None):
    # Assume BST
    # root of tree passed in has no right half (left half could also be empty, returning 'None')
    if current_node.right is None and parent_node is None:
      return current_node, current_node.left

    if current_node.right is None:
      parent_node.right = None
      return current_node, parent_node
    else:
      self.pop_max(current_node.right, current_node)


  def print_tree(self, node=None):
    # Print Tree
    if node is None:
      node = self.root

    if node.left is not None and node.right is not None:
      print "%s -L/R> %s, %s" %(node.value, node.left.value, node.right.value)
      self.print_tree(node.left)
      self.print_tree(node.right)

    elif node.left is not None:
      print "%s -L-> %s" %(node.value, node.left.value)
      self.print_tree(node.left)

    elif node.right is not None:
      print "%s -R-> %s" %(node.value, node.right.value)
      self.print_tree(node.right)


if __name__ == "__main__":

  root = Node(15)
  nodes = [Node(10), Node(20), Node(8), Node(12), Node(17), Node(25), Node(6), Node(11), Node(16), Node(27)]
  t = Tree(root)
  for node in nodes:
    t.add_to_tree(node)
  
  print "\nConstructed Tree:"  
  t.print_tree()
  print "\nIs a Binary Search Tree: ", t.is_bst()
  
  t.remove_node(10)
  print "\nAfter Removing node with value of 10:"
  t.print_tree()
  print "\nIs a Binary Search Tree: ", t.is_bst()

  t.remove_node(6)
  print "\nAfter Removing node with value of 6:"
  t.print_tree()
  print "\nIs a Binary Search Tree: ", t.is_bst()

  t.remove_node(12)
  print "\nAfter Removing node with value of 6:"
  t.print_tree()
  print "\nIs a Binary Search Tree: ", t.is_bst()
