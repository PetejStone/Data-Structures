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
    # Check if the current value is the target, if so, we are done.
    if self.value == target:
      return True
    # If not, left or right based on bigger or smaller, then call contains again (recursion)
    else:
      if target < self.value:
        # Go left
        if not self.left:
          return False
        else:
          return self.left.contains(target)
      else:
        #go right
        if not self.right:
          return False 
        else:
          return  self.right.contains(target)
        
  def get_max(self):
    #max node == farthest to the right
    #base case
    if no right, root is max
    if not self.right:
      return self.value #root
    return self.right.get_max()

    ##iterative solution
    # max_value = self.value
    # current = self
    # while current:
    #   max_value = current.value
    #   current = current.right
    # return max_value


  def for_each(self, cb):
    pass