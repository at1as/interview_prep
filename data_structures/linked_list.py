"""
Usage:
  from linked_list import *
  a = Node(3); b = Node(4); c = Node(5); d = Node(6)
  a.next = b; b.next = c; c.next = d; b.previous = a; c.previous = b; d.previous = c
  l = LinkedList()
  l.get_sum(b)    # arg is any node in list
  l.get_length(b) # arg is any node in list
  e = Node(7)
  l.push(c, e)    # first arg is any node in list
  l.pop(c)        # arg is any node in list
  l.print_list(c) # arg is any node in list
"""

class Node(object):
  def __init__(self, value, previous = None, next = None):
    self.previous = previous
    self.next = next
    self.value = value

  def previous(self):
    return self.previous

  def next(self):
    return self.next

  def value(self):
    return self.value

  def previous(self, previous):
    self.previous = previous

  def next(self, next):
    self.next = next

  def value(self, value):
    self.value = value


class LinkedList(object):
  def __init__(self):
    self.head = None
    self.length = 0

  def get_head(self, n):
    while n.previous:
      n = n.previous
    return n

  def get_tail(self, n):
    while n.next:
      n = n.next
    return n

  def get_length(self, node_in_list):
    self.length = 0
    n = node_in_list

    while n.previous is not None:
      n = n.previous

    self.head = n

    while n.next is not None:
      self.length += 1
      n = n.next

    return self.length + 1

  def get_sum(self, node_in_list):
    h = self.get_head(node_in_list)
    list_sum = 0

    while h.next is not None:
      list_sum += h.value
      h = h.next

    return list_sum + h.value

  def push(self, node_in_list, new_node):
    n = node_in_list

    while n.next is not None:
      n = n.next
    
    new_node.previous = n
    n.next = new_node
    

  def pop(self, node_in_list):
    n = node_in_list

    while n.next is not None:
      n = n.next

    new_tail = n.previous
    new_tail.next = None
    n.previous = None

  def print_list(self, node_in_list):
    h = self.get_head(node_in_list)
    nodes = []
    while h.next:
      nodes.append(h.value)
      h = h.next
    
    for node in nodes:
      print "%s -> " %node

