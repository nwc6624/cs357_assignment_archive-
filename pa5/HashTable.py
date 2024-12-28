# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 14:14:43 2023

@author: Noah caulfield
Class: CS 357 Data Structures, Assignmnet 5 HashTable 
        with a chaining collision strategy 
        
Objective: Practice the use and creation of an Abstract 
Data Type (ADT) for a Hashtable with a chaining collision 
strategy in Python.
"""

class HashTable:
    
    # O(buckets), where buckets is the number of buckets to create.
    def __init__(self, buckets=10):
        self.buckets = buckets
        self.table = [[] for _ in range(buckets)]

    # O(1), since it performs a constant number of operations 
    def hash_function(self, key):
        initial_key = abs(hash(key))
        return initial_key % self.buckets
    
    #  O(n), where n is the number of 
    #items in the bucket with the corresponding hash key
    def put(self, key, value):
        hash_key = self.hash_function(key)
        for index, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                self.table[hash_key][index] = (key, value)
                return
        self.table[hash_key].append((key, value))

    #O(n), where n is the number of items in the bucket with the
    #corresponding hash key
    def get(self, key):
        hash_key = self.hash_function(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return item[1]

    #O(n), where n is the number of 
    #items in the bucket with the corresponding hash key
    def search(self, key):
        hash_key = self.hash_function(key)
        for item in self.table[hash_key]:
            if item[0] == key:
                return True
        return None

    #O(n), where n is the number of 
    #items in the bucket with the corresponding hash key
    def remove(self, key):
        hash_key = self.hash_function(key)
        for index, item in enumerate(self.table[hash_key]):
            if item[0] == key:
                self.table[hash_key].pop(index)
                return
        print("Key not found")


    """ O(buckets + n), where buckets is the 
    number of buckets and n is the number of
    items in the hash table.
    """
    def __len__(self):
        count = 0
        for bucket in self.table:
            count += len(bucket)
        return count


    #O(1), since it only compares the length of the
    #hash table to 0.
    def isEmpty(self):
        return len(self) == 0


    """
    O(buckets + n), where buckets is the
    number of buckets and n is the number
    of items in the hash table
    """
    def __str__(self):
        if self.isEmpty():
            return "Hash Table is Empty"
        result = ""
        for i, bucket in enumerate(self.table):
            result += f"Bucket {i}: "
            if len(bucket) > 0:
                for item in bucket:
                    result += f"{item[0]}:{item[1]} -> "
            result += "\n"
        return result