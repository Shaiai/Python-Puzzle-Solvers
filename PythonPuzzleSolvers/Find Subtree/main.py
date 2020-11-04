"""
Find subtree

Given 2 binary trees t and s, find if s has a n equal subtree in t, where the structure and the values are the same. Return True if it exists, otherwise return False.

"""

class Node():
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right
 
def __repr__(self):
  return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def find_subtree(s,t):

  def preorder_traversal(node):
    if node is None:
      return ''
    return str(node.value) + '-' + preorder_traversal(node.left) + '-' + preorder_traversal(node.right)

  return preorder_traversal(s) in preorder_traversal(t)



t3 = Node(4, Node(3), Node(2))
t2 = Node(5, Node(4), Node(-1))
t = Node(1, t2, t3)

s = Node(4, Node(3), Node(2))

print(find_subtree(s,t))