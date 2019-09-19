import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  #

  def insert(self, value):
    #current node is self
    #check if self.value is > or < than new value -- left or right
    if value < self.value:
    #We go left or right, then check if node exists
      if not self.left:
    #if node does not exists, create it
        self.left = BinarySearchTree(value)
    #if node does exist, use recursion! Call insert on that specific node
      else:
        self.left.insert(value)
    else:
       #we go right
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)



  def contains(self, target):
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass