"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length
  
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""
  def add_to_head(self, value): ## prepend
    if self.head is None: #if nothing is in list
      new_node = Node(value) #create a new node and pass in the data (value)
      new_node.prev = None # Previous node is None since it will be placed at the beginning
      self.head = new_node # the head element is now = to the new node
    else: #if list has at least one item
      new_node = Node(data) #create new node as set it's value to the data
      self.head.prev = new_node # the CURRENT head's previous node (now None) should be changed to the new node that will be taking it's place
      new_node.next = self.head # the newly created node's next node should point to the current head (which will no longer be the head after the node is placed -- think of 'self.head' as a VALUE statement, not a location)
      self.head = new_node #make the head the new node 
      new_node.prev = None ## set the new node's prev to None because it is the NEW HEAD
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    pass

   """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value): ## append
    if self.head is None: #If nothing is in the list
      new_node = ListNode(value) #Create a new node and pass in the data (or value)
      new_node.prev = None # Previous node is None since it is the beginning of the list
      self.head = new_node #the head node element is new the newly created node
    else: #if there is at least one element in the list
      new_node = Node(value) # create new node
      #go through each item and check if Next is == None until you find it
      #this is the last item 
      cur = self.head # start a current variable at the head
      while cur.next: #while cur has a next, aka -- not = none
        cur = cur.next # set each item you get to as the new current element
        #above will exit when it is at the last node
      cur.next = new_node #set the current item's (the item that WAS last) next node to the new node
      new_node.prev = cur #We want the newly created node's previous node to be the current item (last one in the list)
      new_node.next = None #newly created node points to None since it is the last item
  
  
  
  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    pass

  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    pass

  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    pass

  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    cur = self.head # set current item to the head

    while cur: #while cur is not Null, so while list is NOT empty
      if cur.value == key and cur == self.head: #if the current value is equal to the value we want to delete, and if it's currently at the head of the list
       
        ##Case 1 -- when the Node you want to delete is the head node, and it is also the only item
        if not cur.next #If not pointing to any node -- only node in list
          cur = None # Removes current node we created for checking
          self.head = None #removes node that matched, removes the head
          return ## List is now empty, return
        
        #Case 2 - Delete Head node, but list is not empty (there is a next node)
        else: #opposite of line 113, if next is pointing to a valid node
          nxt = cur.next # set nxt == to the cur.next (the next item in the list (next to the head))
          cur.next = None #We want to remove the pointer to the next item because it is being removed
          #cur.prev = None  --- commented out because not needed, because head's previous already points to none
          nxt.prev = None # setting this == to None because it's current prev was the deleted item
          cur = None #get rid of element by setting it equal to None
          self.head = nxt #move the status of the head to the nxt item
          return #return the list

        
      elif cur.data == key #if data = key, but is not the head (elif from line 110)
          #Case 3 -- When cur.next is NOT none, and NOT the head (if it has a prev and a next)
          if cur.next: #if cur.next is true 
            nxt = cur.next #set nxt to the next item
            prev = cur.prev #set prev to the prev item -- see below
            ##### ---- so in   A  B  C, if B is the cur, then cur.next (nxt) is C, and cur.prev (prev) is A
            #### this is so we can get these to point to each other, looping around the 'deleted' item
            prev.next = nxt #  so A.next is == C, skipping B
            nxt.prev = prev # so C.prev == A skipping B
            
            #kill off pointers that aren't doing anything
            cur.next = None
            cur.prev = None
            cur = None #Get rid of node
            return # return list

          #Case 4 if cur.next IS none, so if it is the tail
          else: #if cur.next is none
            prev = cur.prev # set the prev variable to the previous item
            prev.next = None # Set to none because it will become the new tail
           
           #kill off pointers that aren't doing anything
            cur.prev = None
            cur = None # get rid of node
            return #return the list










      
  """Returns the highest value currently in the list"""
  def get_max(self):
    pass
