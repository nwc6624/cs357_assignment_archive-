"""
Created on Wed Mar 15 17:11:11 2023

Author: Noah Caulfield
Class: CS 357 
Assignment: P3
"""

'''
PA3 Node class provided below 

-----------------

O(1).  data, prev, and next attributes of an object 
of the class below. The complexity of this method is
 constant as we are not depending on nay external factors.
'''
class Node:
    def __init__(self, data):
        #Constructor for the class 
        self.data = data
        self.prev = None
        self.next = None
