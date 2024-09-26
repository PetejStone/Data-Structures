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
      if not self.left: # if there is no left node
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
      if target < self.value: #If less
        # Go left
        if not self.left: #if you cannot go left and there is no left node
          return False
        else:
          return self.left.contains(target) #use recursion to go left until you can't
      else:
        #go right
        if not self.right: #if you cannot go right and there is no right node
          return False 
        else:
          return  self.right.contains(target) #use recursion to go right until you can't
        
  def get_max(self):
    #max node == farthest to the right
    #base case
    #if no right, root is max
    if not self.right:
      return self.value #root
    return self.right.get_max() # keep going right until you can't to get max

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
    ##no need for 'return' because we aren't trying to obtain a value, just perform an operation
    if self.left:
      self.left.for_each(cb) # go left while you can -- 
    if self.right:
      self.right.for_each(cb) #go right while you can

# DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_dft(node,self): 

    if self: 
  
        # Use recursion to go left
        self.in_order_dft(self.left) 
  
        # then print the data of node 
        print(self.value), 
  
        # use recursion to go right
        self.in_order_dft(self.right) 
  
  
  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
      storage = Queue()
      current = self

      while current:
        print(current.value)
        if current.left: # If can go left 
          storage.enqueue(current.left) #call the go left fn and go left
        if current.right: # if can go right
          storage.enqueue(current.right) #call the right fn and go right
        current = storage.dequeue() #call the dequeue fn to pop of the item
        
  

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
      storage = Stack()
      current = self
     
      storage.push(current)
      # current = storage.pop() #call the pop fn
      
      while storage.len() > 0:
        current = storage.pop() #call the pop fn
        print(current.value)
        if current.left:
          storage.push(current.left)
        if current.right:
          storage.push(current.right)
      
      
      
      

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      storage = Stack()
      current = self
     
      storage.push(current)
      # current = storage.pop() #call the pop fn
      
      while storage.len() > 0:
        current = storage.pop() #call the pop fn
        print(current.value)
        if current.right:
          storage.push(current.right)
        if current.left:
          storage.push(current.left)

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    if self.left:
      self.left.post_order_dft(self.left)
    if self.right:
      self.right.post_order_dft(self.right)
    print(self.value)

      
      
      
      