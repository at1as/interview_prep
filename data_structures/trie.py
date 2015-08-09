"""
 Usage: 

 from trie import *;
 t = Trie()
 t.add_term("Hello", "A formal greeting")
 t.add_term("Hey", "An informal greeting")
 t.add_term("Hell", "I hear it is a nice place")
 t.add_term("Bye", "Farewell")
 t.define("Hello")
 t.define("Hey")
 t.define("Hell")
 t.defined_terms()
 t.remove_term("Hell")
 t.defined_terms()
"""

class Node(object):
  def __init__(self, value, definition = None):
    self.value = value
    self.definition = definition
    self.children = {}

  def get_value(self):
    return self.value
  
  def get_child(self, name):
    return self.children[name]

  def get_children(self):
    return self.children

  def get_definition(self):
    return self.definition

  def add_definition(self, definition):
    self.definition = definition

  def remove_definition(self):
    self.definition = None

  def add_child(self, node):
    self.children[node.get_value()] = node

  def remove_child(self, node):
    try:  
      self.children.pop(node.get_value(), None)
    except KeyError:
      pass


class Trie(object):
  def __init__(self):
    self.root = Node(None)

  def add_term(self, word, definition):
    # Add a term to the dictionary
    current_node = self.root

    # Create all nodes for all letters not already defined in the word
    for letter in word:
      try:
        current_node = current_node.children[letter]
      except KeyError:
        tmp = Node(letter)
        current_node.add_child(tmp)
        current_node = tmp
    current_node.add_definition(definition)

  def remove_term(self, word):
    # Delete a term from the the dictionary
    node_path = []
    current_node = self.root

    # Traverse to last node
    for letter in word:
      try:
        node_path.append(current_node.children[letter])
        current_node = current_node.children[letter]
      except KeyError:
        return "%s not in dictorary" %(word)

    # If term is still the root of another term, only delete the definition at the node
    if node_path[-1:][0].get_children():
      node_path[-1:][0].remove_definition()
    else:
      # Delete all nodes back to root for word, or until a branch to another term is reached
      for idx in range(len(node_path) - 1, -1, -1):
        print node_path[idx].get_children()
        if len(node_path[idx].get_children()) == 0:
          node_path[idx - 1].remove_child(node_path[idx])
        else:
          break


  def define(self, word):
    # Traverse trie until word is find and return definition
    current_node = self.root
    for letter in word:
      try:
        current_node = current_node.children[letter]
      except KeyError:
        return "%s not defined in dictionary" %word
    return current_node.get_definition()


  def defined_terms(self, n=None, letter_buffer=""):
    if n is None:
      n = self.root
    
    try:
      letter_buffer += n.get_value()
    except: 
      pass
    
    children = n.get_children()
    if not children:
      return [letter_buffer, n.get_definition()]
    else:
      if n.get_definition():
        return [letter_buffer, n.get_definition()], [self.defined_terms(children[child], letter_buffer) for child in children]
      else:
        return [self.defined_terms(children[child], letter_buffer) for child in children]

