# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 16:39:16 2023

@author: Noah Caulfield
Class: CS 357
PA2:List-based Array
"""

class Array:
    def __init__(self, capacity=10):   # Big-O is O(complexity)
        self.array = [None] * capacity
        self.length = 0

    def isEmpty(self):                   # Big-O is O(1)
        return self.length == 0
       

    def append(self, new_item):          # Big-O is O(1)
        if self.length == len(self.array):
            self.resize(len(self.array) * 2)
        self.array[self.length] = new_item
        self.length += 1

    def resize(self, new_allocation_size):       # Big-O is O(n) where n is length of list 
        new_array = [None] * new_allocation_size
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array
        print("           Resizing... ")

    def prepend(self, new_item):                # Big-O is O(n) where n is length of list 
        if self.length == len(self.array):
            self.resize(len(self.array) * 2)
        for i in range(self.length, 0, -1):
            self.array[i] = self.array[i-1]
        self.array[0] = new_item
        self.length += 1

    def insert_after(self, index, new_item):   # Big-O is O(n) where n is number of elements to right of 'index' position
        if self.length == len(self.array): 
            self.resize(len(self.array) * 2)
        for i in range(self.length, index, -1):
            self.array[i] = self.array[i-1]
        self.array[index+1] = new_item
        self.length += 1

    def search(self, item):                      # Big-O is O(n) where n is length of list
        for i in range(self.length):
            if self.array[i] == item:
                return i
        return -1

    def remove_at(self, index):          # Big-O is O(n) where n is number of elements to right of 'index' position
        if self.isEmpty():
            print("The array is empty.")
            return -1
        if index < 0 or index >= self.length:
            return
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i+1]
        self.length -= 1
        if self.length < len(self.array) * 0.25:
            self.resize(round(len(self.array) * 0.25))

    def remove(self):                               # Big-O is O(1)
        if self.isEmpty():
            print("The array is empty.")
            return -1
        self.length -= 1
        if self.length < len(self.array) * 0.25:
            self.resize(round(len(self.array) * 0.25))

    def __getitem__(self, index):                  # Big-O is O(1)
        if index < 0 or index >= self.length:
            return
        return self.array[index]

    def __setitem__(self, index, item):             # Big-O is O(1)        
        if index < 0 or index >= self.length:
            return
        self.array[index] = item

    def __repr__(self):                            # Big-O is O(n) where n is length of Array
        return str(self.array[:self.length])

    def __len__(self):                          # Big-O is O(1)  
        return self.length