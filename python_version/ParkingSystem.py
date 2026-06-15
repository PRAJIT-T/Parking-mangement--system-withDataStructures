from CustomLinkedList import CustomLinkedList
from BinarySearchTree import BinarySearchTree
from AVLTree import AVLTree

class ParkingSystem:
    def __init__(self, n, tree_type=0):
        if tree_type == 0:
            self.tree = BinarySearchTree()
        elif tree_type == 1:
            self.tree = AVLTree()
        else:
            self.tree = BinarySearchTree()

        self.queue = CustomLinkedList()
        self.tree.create_tree(n)

        self.current_size = 0
        self.max_size = n
        self.occupancy_percentage = 0

    def update_status(self):
        self.occupancy_percentage = int((self.current_size / self.max_size) * 100)
        return

    def get_occupancy_status(self):
        return f"Occupancy: {self.current_size}/{self.max_size}"

    def get_occupancy_percentage(self):
        return self.occupancy_percentage
    
    def add_car(self, reg_no):
        if self.queue.head is not None:
            QueueNode = self.queue.head
            while QueueNode is not None:
                if QueueNode.reg_no == reg_no:
                    return QueueNode.spot_id
                QueueNode = QueueNode.right
        if self.current_size >= self.max_size:
            print("Parking is full")
            return
        node = self.tree.remove_spot(self.tree.search_for_free_spot())
        self.queue.enqueue(node)
        node.set_reg_no(reg_no)
        self.current_size += 1
        self.update_status()
        return self.queue.print_last_spotID()
    
    def last_spotID(self):
        return self.queue.print_last_spotID()

    def remove_car(self, reg_no):
        node = self.queue.find_and_pop(reg_no)
        if node:
            node.set_reg_no(None)
            self.tree.insert_spot(node)
            self.current_size -= 1
            self.update_status()
        else:
            print(f"Car with registration {reg_no} not found")
    
    def print_tree(self):
        self.tree.print_tree()
    
    def print_queue(self):
        self.queue.print_queue()