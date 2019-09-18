import sys
sys.path.append('../doubly_linked_list') 
from doubly_linked_list import DoublyLinkedList

import sys
sys.path.append('./doubly_linked_list') 
from doubly_linked_list import ListNode

class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.dict = dict() #instantiates dictionary
    self.head = ListNode(0,0)
    self.tail = ListNode(0,0)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.storage = DoublyLinkedList()

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.dict: #if key value is in the dictionary
      #if there, update it so it is the most recently used -- by removing and re adding
      node = self.dict[key]
      self.storage.remove_from_tail()#remove
      self.storage.add_to_tail(node)# re add
      return node.value
    return -1 # -1 means not there

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if key in self.dict:
      self.storage.remove_from_tail()
    node = ListNode(key,value)
    self.storage.add_to_tail(node)
    self.dict[key] = node
    if len(self.dict) > self.limit:
      node = self.head.next
      self.storage.remove_from_tail(node)
      del self.dict[node.key]

