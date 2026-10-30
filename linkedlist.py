# Linked list: A data structure consisting of nodes, where each node contains data and a reference to the next node in the sequence.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=Node(data)
        # LinkedList is empty
        if self.head is None:
            self.head=new_node
        # LinkedList is not Empty
        new_node.next=self.head
        self.head=new_node

    def insert_at_ending(self,data):
        new_node=Node(data)
        # LinkedList is empty
        if self.head is None:
            self.head= new_node
        # LinkedList is not empty
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def insert_at_position(self,position,data):
        if position<0:
            print('Invalid Position')
        if position==0:
            self.insert_at_beginning(data)
        # if position is 1 or more
        new_node = Node(data)
        current=self.head
        for _ in range(position-1):
            current = current.next
        new_node.next=current.next
        current.next=new_node

    def delete_at_beginning(self):
        # LinkedList is empty
        if self.head is None:
            print('Linked List is Empty')
            return 
        # LinkedList has only one element
        if self.head.next is None:
            self.head= None
            return 
        # LinkedList has more than one element
        self.head= self.head.next

    def delete_at_ending(self):
        if self.head is None:
            print('Linked List is Empty')
            return 
        # LinkedList has only one element
        if self.head.next is None:
            self.head= None
            return 
        # LinkedList has more than one element
        current=self.head
        while current.next.next is not None:
            current=current.next
        current.next=None

        
