"""
Created on Wed Mar 15 17:11:11 2023

Author: Noah Caulfield
Class: CS 357 
Assignment: P3

PA3 DoubleLinkedList class provided, utilizing
all methods listed per spec sheet.

Brief explanation for context: 
A doubly linked list is a type of data structure 
used in CS to store and manage collections of elements.
 In a doubly linked list, each element, also known as a 
 node, contains a value and two pointers, one pointing
 to the previous node and one pointing to the next node 
 in the list. This allows for efficient traversal
 of the list in both directions, as each node can be 
 accessed from either direction.

In Python, you can implement a doubly linked list
 by creating a Node class to represent each node in 
 the list, and a DoublyLinkedList class to manage the 
 list itself.

"""

class DLinkedList:
    
    #Running times are labeled above where applicable
    
    #O(1), which means that the time complexity of the code is constant.
    def __init__(self):
        # Constructor initializes the head, tail, and size 
        self.head = None
        self.tail = None
        self.size = 0
    #0(1), As it returns the value of the attribute size, which is constant in time 
    def __len__(self):
        #method to return length of list 
        return self.size

    #O(1), Only involves a single comparison operation
    def isEmpty(self):
        #Method to check if list is empty; T/F return 
        return self.size == 0
    '''
    O(n), where n is the number of nodes in the linked list
    #The bits outside the while loop take constant time,
    so their time complexity is O(1). However, all other 
    elements share 0(n) complexity so heirarchy prevails
    '''
    def reverse(self):
        #Method to reverse order of the list 
        current_node = self.head
        while current_node is not None:
            temp = current_node.prev
            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp
    '''
    O(1). Regardless of the size of the list, the number 
    of operations performed by the method is constant.
    '''
    def append(self, new_node):
        '''
        Method to append new node to end of list.
         Recieves a node object .
         Method then updates the list size parameters.
         '''
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    '''
    O(1). No matter size of list, the number of operations 
    performed by prepend() remains constant.
    
    '''
    def prepend(self, new_node):
        '''
        Method to prepend new node to the front of the list.
        Method recieves node object.
        Method updates the size of the list
        '''
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        '''
        O(1).The size of the linked list and the position of 
        the current node where the new node will be inserted
        dictates the overall complexity.
        '''
    def insert_after(self, current_node, new_node):
        '''
        Method to insert node after another node.
        Method inserts after current node then updates list size.
        check if empty, check if current node is last node.
        '''
        if current_node is None: 
            return
        if current_node == self.tail:
            self.append(new_node)
        else:
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
            new_node.prev = current_node
        self.size += 1
        '''
        O(1). The Number of operations 
        performed by this method does not depend on the 
        size of the input- execution time is constant
        '''

    def insert_before(self, current_node, new_node):
        '''
        Method for inserting before new node.
        Method recieves current_node and the new node.
        insert new node before current node.
        Update size of list.
        Check if list is empty.
        Is current_node first?
        '''
        if current_node is None:
            return
        if current_node == self.head:
            self.prepend(new_node)
        else:
            new_node.prev = current_node.prev
            current_node.prev.next = new_node
            current_node.prev = new_node
            new_node.next = current_node
        self.size += 1

        '''
        0(n), where n is the size of the linked list. The biggest/
        worst scenario ia when the node is to be removed at the 
        end of said linked list. The entire list then has to be 
        traversed to the tail end.
        '''
    def remove(self, current_node):
        '''
        Method for removing a given node from a list.
        Update size of list.
        '''
        if current_node is None:
            return
        if current_node == self.head:
            self.head = current_node.next
        if current_node == self.tail:
            self.tail = current_node.prev
        if current_node.prev is not None:
            current_node.prev.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = current_node.prev
        self.size -= 1

        '''
        O(1). When current_node is the head/top of the list, 
        no removal is required, so the method exits without 
        further computation. Otherwise, it updates the head
        of the list and calls the remove() method.
        '''


    def remove_before(self, current_node):
        '''
        Method for removing node before given node.
        Update list size
        Check if current_node is head of list, therefore  no removal
        '''
        if current_node is None or current_node == self.head:
            return
        if current_node.prev == self.head:
            self.head = current_node
        self.remove(current_node.prev)

        ''' O(1). When current_node is the tail of the list, 
        no removal is done, so the method exits without further computation.
         Otherwise, it updates the tail of the list 
         and calls the remove() method.
         '''
    def remove_after(self, current_node):
        '''
        Method for removing node after given node.
        Update list size
        Check if current_node is tail of list, therefore  no removal
        '''
        if current_node is None or current_node == self.tail:
            return
        if current_node.next == self.tail:
            self.tail = current_node
        self.remove(current_node.next)
        '''
        O(n). For the worst case  instance involves
        the method needing to traverse the entire list 
        to search for the node with the given value.
        '''
    def search(self, value):
        '''
        Method to search for node of particular value.
        Method returns position, otherwise return -1.

        '''
        current_node = self.head
        position = 0
        while current_node is not None:
            if current_node.data == value:
                return position
            current_node = current_node.next
            position += 1
        return -1

    '''O(n), where n is the size of the linked list.
    This is because worst case it has to traverse the entire
    list to create the list representation as a string. 
    '''
    def __repr__(self):
        '''
        Method to show contents of list
        Return the list!
        '''
        current_node = self.head
        nodes = [ ]
        while current_node is not None:
            nodes.append(str(current_node.data))
            current_node = current_node.next
            #spacing for printing of nodes between brackets below
        return '[{}]'.format(' '.join(nodes))  

