from Node import Node
class Tree:
    def __init__(self):
        self.root = None
    
    def clear_tree(self):
        self._delete_sub_tree(self.root)
        self.root = None
    
    def _delete_sub_tree(self, node):
        if node is None:
            return
        self._delete_sub_tree(node.left)
        self._delete_sub_tree(node.right)
        
        node.left = None
        node.right = None
        node.parent = None
    
    def search_for_free_spot(self):
        # Abstract method to be implemented by subclasses
        pass
    
    def remove_spot(self, node):
        # Abstract method to be implemented by subclasses
        pass
    
    def insert_spot(self, node):
        # Abstract method to be implemented by subclasses
        pass
    
    def print_tree(self):
        print("Printing Tree Structure:")
        if self.root is None:
            print("Tree is empty")
            return
        self._print_tree_recursive(self.root, 0, "Root: ")
    
    def _print_tree_recursive(self, node, level, prefix):
        if node is None:
            return
        
        indent = "  " * level
        print(f"{indent}{prefix}Spot ID: {node.spot_id}")
        
        if node.left is not None or node.right is not None:
            if node.left is not None:
                self._print_tree_recursive(node.left, level + 1, "L-> ")
            else:
                print(f"{indent}  L-> null")
            
            if node.right is not None:
                self._print_tree_recursive(node.right, level + 1, "R-> ")
            else:
                print(f"{indent}  R-> null")

