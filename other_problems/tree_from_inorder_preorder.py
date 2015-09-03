class Node(object):

  # Standard Binary Node
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right


def split_lists(in_ord, local_root):
  
  # Left Side
  # Create array from beginning of in_ord array until local_root is reached
  ls = []
  ls_limit = 0
  for idx, x in enumerate(in_ord):
    if x == local_root:
      ls_limit = idx
      break
    
    ls = ls + [x]

  # Right Side
  # Create array from after local_root until the end of in_ord array
  rs = []
  for x in in_ord[ls_limit + 1:]:
    rs = rs + [x]

  return ls, rs, ls_limit


def build_tree(inorder, preorder, runs=0):
  global root_node

  # Root Node
  local_root = Node(preorder[0])
  preorder = preorder[1:]

  # Set local root to global root_node so that it can be retreived by the main method
  if runs == 0: 
    root_node = local_root

  # Split the inorder list at 
  ls, rs, idx = split_lists(inorder, local_root.value)


  if len(ls) > 1:
    local_root.left = build_tree(ls, preorder[:idx], runs + 1)
  elif len(ls) == 1:
    local_root.left = Node(ls[0])
  
  if len(rs) > 1:
    local_root.right = build_tree(rs, preorder[idx:], runs + 1)
  elif len(rs) == 1:
    local_root.right = Node(rs[0])

  return local_root

def node_walk(root):
  if root.left is not None and root.right is not None:
    print "%s <- %s -> %s" %(root.left.value, root.value, root.right.value)
    node_walk(root.left)
    node_walk(root.right)

  elif root.left is not None:
    print "%s <- %s -> NONE" %(root.left.value, root.value)
    node_walk(root.left)

  elif root.right is not None:
    print "NONE <- %s -> %s" %(root.value, root.right.value)
    node_walk(root.right)

  else:
    print "NONE <- %s -> NONE" %(root.value)


if __name__ == "__main__":
  # Reconstruct a Tree given both an inorder and preorder list
  # http://www.careercup.com/question?id=5179541339242496

  root_node = None
  
  in_order = [1, 7, 3, 4, 2, 8, 9]
  pre_order = [4, 7, 1, 3, 8, 2, 9]

  build_tree(in_order, pre_order)

  node_walk(root_node)
  