from Node import Node
from Tree import Tree 

class BinarySearchTree(Tree):
    def search_for_free_spot(self):
        """
        Finds the node with the smallest spot_id (leftmost node).
        Returns:
            Node: The node object with the smallest spot_id, or None if the tree is empty.
        """
        if self.root is None:
            return None

        current = self.root
        # No need for the initial check 'if current.left is None', the while loop handles it.
        while current.left is not None:
            current = current.left
        return current # Return the node object

    def create_tree(self, number_of_nodes):
        """
        Creates a balanced Binary Search Tree from a given number of spots.
        Args:
            number_of_nodes (int): The total number of spots (e.g., 10 creates spots 1 to 10).
        """
        if number_of_nodes <= 0:
            self.root = None
            return
        spots = [i + 1 for i in range(number_of_nodes)]
        # Pass parent=None for the initial root creation
        self.root = self._create_balanced_bst_recursive(spots, 0, number_of_nodes - 1, None)

    def _create_balanced_bst_recursive(self, spots, start, end, parent):
        """
        Recursively creates a balanced BST node and links its children and parent.
        Args:
            spots (list): The list of spot IDs.
            start (int): Starting index for the current subtree.
            end (int): Ending index for the current subtree.
            parent (Node or None): The parent of the node being created.
        Returns:
            Node: The root node of the created subtree.
        """
        if start > end:
            return None

        mid = (start + end) // 2
        node = Node(spots[mid])
        node.parent = parent # Set parent during creation

        # Recursively create left and right subtrees, passing the current node as their parent
        node.left = self._create_balanced_bst_recursive(spots, start, mid - 1, node)
        node.right = self._create_balanced_bst_recursive(spots, mid + 1, end, node)

        return node

    def _find_minimum(self, node):
        """ Finds the node with the minimum key in the subtree rooted at node """
        if not node:
            return None
        while node.left is not None:
            node = node.left
        return node

    def _transplant(self, u, v):
        """
        Replaces the subtree rooted at node u with the subtree rooted at node v.
        Handles updating parent pointers correctly.
        Args:
            u (Node): The node to be replaced.
            v (Node or None): The node to replace u with.
        """
        if u.parent is None: # u is the root
            self.root = v
        elif u == u.parent.left: # u is a left child
            u.parent.left = v
        else: # u is a right child
            u.parent.right = v

        if v is not None: # Update v's parent pointer
            v.parent = u.parent

    def remove_spot(self, node_to_delete):
        """
        Removes a node from the BST.
        It finds the actual node in the tree corresponding to node_to_delete's spot_id.
        Handles cases for 0, 1, or 2 children using the transplant helper.
        For the 2-child case, it replaces the node's data with its successor's data
        and then removes the successor node.

        Args:
            node_to_delete (Node): A node object whose spot_id should be removed.
                                   This might not be the exact instance from the tree.
        Returns:
            Node: A *new* Node object containing the spot_id and reg_no of the
                  logically removed spot, detached from the tree. Returns None
                  if the node wasn't found.
        """
        if node_to_delete is None or self.root is None:
            return None # Node not provided or tree empty

        # --- Find the actual node instance in the tree ---
        # This is important because node_to_delete might just have the ID,
        # not be the actual object connected in the tree structure.
        node = self.find_node_by_spot_id(node_to_delete.spot_id)
        if node is None:
             # The spot ID requested for removal wasn't found in the tree
             print(f"Warning: Node with spot ID {node_to_delete.spot_id} not found in BST for removal.")
             return None

        # --- Prepare the node to return ---
        # Create a *copy* of the node data that is being logically removed.
        # This node will be detached from the tree.
        returned_node = Node(node.spot_id)
        returned_node.set_reg_no(node.reg_no) # Preserve registration number

        # --- Perform BST Deletion ---
        if node.left is None:
            # Case 1: No left child (includes leaf node case)
            self._transplant(node, node.right)
        elif node.right is None:
            # Case 2: No right child
            self._transplant(node, node.left)
        else:
            # Case 3: Node has two children
            # Find the inorder successor (minimum node in the right subtree)
            successor = self._find_minimum(node.right)

            # The node being returned *must* have the original spot_id
            # (already handled above when creating returned_node)

            if successor.parent != node:
                # If successor is not the direct right child:
                # 1. Replace successor with its own right child (it has no left child)
                self._transplant(successor, successor.right)
                # 2. Link successor's right child correctly to node's right subtree
                successor.right = node.right
                successor.right.parent = successor
            # else: successor is the direct right child, transplant below handles parent update

            # Replace the node to be deleted (node) with the successor
            self._transplant(node, successor)
            # Link successor's left child correctly to node's left subtree
            successor.left = node.left
            successor.left.parent = successor

        # --- Clean up pointers of the physically removed node ---
        # Help garbage collection and prevent dangling references
        node.parent = node.left = node.right = None

        # Return the detached node with the original data
        return returned_node

    def find_node_by_spot_id(self, spot_id):
         """ Finds and returns the actual node object in the tree with the given spot ID """
         current = self.root
         while current is not None:
             if spot_id == current.spot_id:
                 return current
             elif spot_id < current.spot_id:
                 current = current.left
             else:
                 current = current.right
         return None # Not found


    def insert_spot(self, node):
        """
        Inserts a node into the BST. Assumes the node is not already present.
        Args:
            node (Node): The node object to insert. Its left/right/parent should be None.
        """
        if node is None:
             print("Warning: Attempted to insert None node.")
             return # Do nothing if node is None

        # Reset pointers just in case the node is being reused (good practice)
        node.left = None
        node.right = None
        node.parent = None

        if self.root is None:
            self.root = node
            return # Tree was empty

        current = self.root
        parent = None
        while current is not None:
            parent = current # Keep track of the parent
            if node.spot_id < current.spot_id:
                current = current.left
            elif node.spot_id > current.spot_id:
                current = current.right
            else:
                # Duplicate spot ID found - this shouldn't happen with free spots logic
                # but good to handle defensively.
                print(f"Warning: Trying to insert duplicate spot ID {node.spot_id}. Insertion ignored.")
                return # Ignore insertion

        # Link the new node
        node.parent = parent
        if node.spot_id < parent.spot_id:
            parent.left = node
        else:
            parent.right = node

