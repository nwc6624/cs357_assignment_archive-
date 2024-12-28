# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:38:34 2023

@author: Noah Caulfield


Assignment 4, CS 357
"""


# Queue.py

class Queue:
    
   
    def __init__(self, capacity=10):
        self.items = [None] * capacity
        self.size = 0
        self.front = 0
        self.capacity = capacity
        print("Queue created")

    def __len__(self):
        return self.size

    def __repr__(self):
        return str(self.items)

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[self.front]
#O(1), because it performs a constant number of operations regardless of the size of the queue. 
    def dequeue(self):    
        if self.isEmpty():
            print("Empty")
            return None
        else:
            front_e = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            if self.size < self.capacity // 4:
                print("           Resizing...")
                self.resize(self.capacity // 4)
            print(f"Removing. New Front: {self.front}")
            return front_e
        
'''O(n),because it copies all elements of the
 queue to a new array with a larger capacity'''
    def enqueue(self, item):
        if self.size == self.capacity:
            print("Resizing...")
            self.resize(2 * self.capacity)
        self.items[(self.front + self.size) % self.capacity] = item
        self.size += 1
        print(f"Inserting at index: {(self.front + self.size - 1) % self.capacity}")

#O(n), where n is the size of the queue
    def resize(self, new_cap):
        new_items = [None] * new_cap
        for i in range(self.size):
            new_items[i] = self.items[(self.front + i) % self.capacity]
        self.items = new_items
        self.capacity = new_cap
        self.front = 0

