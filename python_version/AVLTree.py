from Node import Node
from Tree import Tree

class AVLTree(Tree):
    def height(self, node):
        if node is None:
            return -1
        return node.height
    
    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update parent pointers
        if T2 is not None:
            T2.parent = y
        x.parent = y.parent
        y.parent = x
            
        # Update root if needed
        if y == self.root:
            self.root = x
        else:
            if x.parent.left == y:
                x.parent.left = x
            else:
                x.parent.right = x
        
        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update parent pointers
        if T2 is not None:
            T2.parent = x
        y.parent = x.parent
        x.parent = y
            
        # Update root if needed
        if x == self.root:
            self.root = y
        else:
            if y.parent and y.parent.left == x:
                y.parent.left = y
            elif y.parent:
                y.parent.right = y
        
        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        
        return y

    def _rebalance(self, node):
        while node is not None:
            # Update height of the current node
            node.height = max(self.height(node.left), self.height(node.right)) + 1

            # Get balance factor
            balance = self.get_balance(node)

            # Left heavy
            if balance > 1:
                if self.get_balance(node.left) >= 0:
                    node = self.right_rotate(node)
                else:
                    node.left = self.left_rotate(node.left)
                    node = self.right_rotate(node)
            # Right heavy
            elif balance < -1:
                if self.get_balance(node.right) <= 0:
                    node = self.left_rotate(node)
                else:
                    node.right = self.right_rotate(node.right)
                    node = self.left_rotate(node)

            # Move up the tree
            node = node.parent

    def insert_spot(self, node):
        if node is None:
            return
            
        # First do normal BST insert
        if self.root is None:
            self.root = node
            node.parent = None
            return
        
        current = self.root
        while True:
            if node.spot_id < current.spot_id:
                if current.left is None:
                    current.left = node
                    node.parent = current
                elif current.right is None:
                    current.right = node
                    node.parent = current
                break
            else:
                if current.right is None:
                    current.right = node
                    node.parent = current
                elif current.left is None:
                    current.left = node
                    node.parent = current
                break
        
        # Rebalance starting from the new node's parent
        self._rebalance(node.parent)

    def remove_spot(self, node_to_delete):
        if node_to_delete is None:
            return None

        # Create return node before modifying tree
        return_node = Node(node_to_delete.spot_id)
        return_node.set_reg_no(node_to_delete.reg_no)

        # Store parent for rebalancing
        parent = node_to_delete.parent

        # Case 1: Node has at most one child
        if node_to_delete.left is None or node_to_delete.right is None:
            replacement = node_to_delete.left if node_to_delete.left else node_to_delete.right

            if replacement is None:  # No children
                if node_to_delete == self.root:
                    self.root = None
                else:
                    if node_to_delete.parent.left == node_to_delete:
                        node_to_delete.parent.left = None
                    else:
                        node_to_delete.parent.right = None
            else:  # One child
                replacement.parent = node_to_delete.parent
                if node_to_delete == self.root:
                    self.root = replacement
                else:
                    if node_to_delete.parent.left == node_to_delete:
                        node_to_delete.parent.left = replacement
                    else:
                        node_to_delete.parent.right = replacement

        # Case 2: Node has two children
        else:
            # Find successor (smallest in right subtree)
            successor = node_to_delete.right
            while successor.left:
                successor = successor.left

            # Copy successor's data to the node being deleted
            node_to_delete.spot_id = successor.spot_id
            node_to_delete.reg_no = successor.reg_no

            # Remove the successor
            if successor.parent.left == successor:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right

            if replacement is not None:
                replacement.parent = node_to_delete.parent
            if successor.right is not None:
                successor.right.parent = successor.parent

            # Update parent for rebalancing
            parent = successor.parent if successor.parent != node_to_delete else node_to_delete

        # Update heights and rebalance the tree
        if parent:
            self._rebalance(parent)

        return return_node

    def search_for_free_spot(self):
        if self.root is None:
            return None
        current = self.root
        while current and current.left:
            current = current.left
        return current

    def create_tree(self, number_of_nodes):
        if number_of_nodes is None:
            return
        spots = [i + 1 for i in range(number_of_nodes)]
        self.root = self._create_balanced_avl(spots, 0, number_of_nodes - 1, None)
    
    def _create_balanced_avl(self, spots, start, end, parent=None):
        if spots is None or start > end:  # Corrected condition
            return None

        mid = (start + end) // 2
        new_node = Node(spots[mid])  # Renamed `node` to `new_node` for clarity
        new_node.parent = parent  # Set parent during creation

        new_node.left = self._create_balanced_avl(spots, start, mid - 1, new_node)
        new_node.right = self._create_balanced_avl(spots, mid + 1, end, new_node)

        return new_node

    def _print_tree_recursive(self, node, level, prefix):
        if node is None:
            return
        print(f"{' ' * (level * 4)}{prefix}{node.spot_id}")
        self._print_tree_recursive(node.left, level + 1, "L---")
        self._print_tree_recursive(node.right, level + 1, "R---")

    def validate_tree(self, node, visited=None):
        if visited is None:
            visited = set()
        if node is None:
            return True
        if node in visited:
            print(f"Circular reference detected at node {node.spot_id}")
            return False
        visited.add(node)
        return self.validate_tree(node.left, visited) and self.validate_tree(node.right, visited)