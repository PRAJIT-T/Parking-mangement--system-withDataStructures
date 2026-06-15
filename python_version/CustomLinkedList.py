from Node import Node
from Tree import Tree
from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree


class CustomLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.right = node
            self.tail = node
    
    def find_and_pop(self, reg_no):
        current = self.head
        previous = None
        while current is not None:
            if current.reg_no == reg_no:
                if previous is None:
                    if current.right is not None:
                        self.head = current.right
                    else:
                        self.head = None
                        self.tail = None
                else:
                    previous.right = current.right
                    if current == self.tail:
                        self.tail = previous
                return current
            previous = current
            current = current.right
        return None
    
    def clear_queue(self):
        if self.head is None:
            return  # Queue is already empty
        
        current = self.head
        while current is not None:
            next_node = current.right
            current.right = None
            current = next_node
        
        self.head = None
        self.tail = None
    
    def print_last_spotID(self):
        if self.tail:
            return self.tail.spot_id

    def print_queue(self):
        print("Printing Queue Contents:")
        if self.head is None:
            print("The queue is empty")
            return
        
        position = 1
        current = self.head
        while current is not None:
            print(f"Position {position}: Spot ID: {current.spot_id}, Registration: {current.reg_no if current.reg_no is not None else 'None'}")
            current = current.right
            position += 1
        print("End of queue")
