import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class Queue(object):
  def __init__(self):
    self.items = []

  def enqueue(self, item):
    self.items.insert(0,item)
  
  def dequeue(self):
    if not self.is_empty():
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[-1].value
  def __len__(self):
    return self.size()

  def size(self):
    return len(self.items)

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
    #if no right, root is max
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
    # Must use a callback function

    cb(self.value)

    #check for left or right then use recursion

    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

# DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(node,self):
  
    # if self:
    #   while self.left:
    #     pass
    #     #self.left.in_order_dft(self.left)
    #   print(self.value)
    #   return
    #   while self.right:
    #     pass
    #     #self.right.in_order_dft(self.right)
      
    #   return
  
      
  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, start):
    if start is None:
      return '123'
    queue = Queue()

    queue.enqueue(start)
    traversal = 0
    while len(queue) > 0:
      traversal += queue.peek() 
      node = queue.dequeue()

      if node.left:
        queue.enqueue(node.left)
      if node.right:
        queue.enqueue(node.right)
    return '123'
      

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
      if self.left:
        self.left
        self.right
      else:
        self.left
        self.right

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass