package DataStructures;

public class AVLTree implements Tree {
    protected Node root = null;

    private int height(Node node) {
        if (node == null) return -1;
        return node.height;
    }

    private int getBalance(Node node) {
        if (node == null) return 0;
        return height(node.left) - height(node.right);
    }

    private Node rotateRight(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        // Perform rotation
        x.right = y;
        y.left = T2;

        // Update parent pointers
        if (T2 != null) T2.parent = y;
        x.parent = y.parent;
        y.parent = x;

        // Update root if needed
        if (y == root) {
            root = x;
        } else {
            if (x.parent != null && x.parent.left == y) {
                x.parent.left = x;
            } else if (x.parent != null) {
                x.parent.right = x;
            }
        }

        // Update heights
        y.height = Math.max(height(y.left), height(y.right)) + 1;
        x.height = Math.max(height(x.left), height(x.right)) + 1;

        return x;
    }

    private Node rotateLeft(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        // Perform rotation
        y.left = x;
        x.right = T2;

        // Update parent pointers
        if (T2 != null) T2.parent = x;
        y.parent = x.parent;
        x.parent = y;

        // Update root if needed
        if (x == root) {
            root = y;
        } else {
            if (y.parent != null && y.parent.left == x) {
                y.parent.left = y;
            } else if (y.parent != null) {
                y.parent.right = y;
            }
        }

        // Update heights
        x.height = Math.max(height(x.left), height(x.right)) + 1;
        y.height = Math.max(height(y.left), height(y.right)) + 1;

        return y;
    }

    private void rebalance(Node node) {
        while (node != null) {
            // Update height of the current node
            node.height = Math.max(height(node.left), height(node.right)) + 1;

            // Get balance factor
            int balance = getBalance(node);

            // Left heavy
            if (balance > 1) {
                if (getBalance(node.left) >= 0) {
                    node = rotateRight(node);
                } else {
                    node.left = rotateLeft(node.left);
                    node = rotateRight(node);
                }
            }
            // Right heavy
            else if (balance < -1) {
                if (getBalance(node.right) <= 0) {
                    node = rotateLeft(node);
                } else {
                    node.right = rotateRight(node.right);
                    node = rotateLeft(node);
                }
            }

            // Move up the tree
            node = node.parent;
        }
    }

    @Override
    public void insertSpot(Node newNode) {
        if (newNode == null) return;

        // Perform normal BST insertion
        if (root == null) {
            root = newNode;
            newNode.parent = null;
            return;
        }

        Node current = root;
        while (true) {
            if (newNode.spotID < current.spotID) {
                if (current.left == null) {
                    current.left = newNode;
                    newNode.parent = current;
                    break;
                }
                current = current.left;
            } else {
                if (current.right == null) {
                    current.right = newNode;
                    newNode.parent = current;
                    break;
                }
                current = current.right;
            }
        }

        // Rebalance the tree starting from the new node's parent
        rebalance(newNode.parent);
    }

    @Override
    public Node removeSpot(Node nodeToDelete) {
        if (nodeToDelete == null) return null;

        // Create a return node before modifying the tree
        Node returnNode = new Node(nodeToDelete.spotID);
        returnNode.setRegNo(nodeToDelete.regNo);

        Node parent = nodeToDelete.parent;

        // Case 1: Node has at most one child
        if (nodeToDelete.left == null || nodeToDelete.right == null) {
            Node replacement = (nodeToDelete.left != null) ? nodeToDelete.left : nodeToDelete.right;

            if (replacement == null) { // No children
                if (nodeToDelete == root) {
                    root = null;
                } else {
                    if (nodeToDelete.parent.left == nodeToDelete) {
                        nodeToDelete.parent.left = null;
                    } else {
                        nodeToDelete.parent.right = null;
                    }
                }
            } else { // One child
                replacement.parent = nodeToDelete.parent;
                if (nodeToDelete == root) {
                    root = replacement;
                } else {
                    if (nodeToDelete.parent.left == nodeToDelete) {
                        nodeToDelete.parent.left = replacement;
                    } else {
                        nodeToDelete.parent.right = replacement;
                    }
                }
            }
        }
        // Case 2: Node has two children
        else {
            Node successor = nodeToDelete.right;
            while (successor.left != null) {
                successor = successor.left;
            }

            // Copy successor's data to the node being deleted
            nodeToDelete.spotID = successor.spotID;
            nodeToDelete.regNo = successor.regNo;

            // Remove the successor
            if (successor.parent.left == successor) {
                successor.parent.left = successor.right;
            } else {
                successor.parent.right = successor.right;
            }

            if (successor.right != null) {
                successor.right.parent = successor.parent;
            }

            parent = successor.parent;
        }

        // Rebalance the tree starting from the parent
        if (parent != null) {
            rebalance(parent);
        }

        return returnNode;
    }

    @Override
    public Node searchForFreeSpot() {
        return findFreeSpot(root);
    }

    private Node findFreeSpot(Node node) {
        if (node == null) return null;

        if (node.regNo == null) return node;

        Node leftResult = findFreeSpot(node.left);
        if (leftResult != null) return leftResult;

        return findFreeSpot(node.right);
    }

    public void createTree(int numberOfNodes) {
        int[] spots = new int[numberOfNodes];
        for (int i = 0; i < numberOfNodes; i++) {
            spots[i] = i + 1;
        }
        root = createBalancedAVL(spots, 0, numberOfNodes - 1, null);
    }

    private Node createBalancedAVL(int[] spots, int start, int end, Node parent) {
        if (start > end) return null;

        int mid = (start + end) / 2;
        Node newNode = new Node(spots[mid]);
        newNode.parent = parent;

        newNode.left = createBalancedAVL(spots, start, mid - 1, newNode);
        newNode.right = createBalancedAVL(spots, mid + 1, end, newNode);

        newNode.height = Math.max(height(newNode.left), height(newNode.right)) + 1;

        return newNode;
    }

    @Override
    public void clearTree() {
        root = null;
    }

    @Override
    public void printTree() {
        printTreeRecursive(root, 0, "Root: ");
    }

    private void printTreeRecursive(Node node, int level, String prefix) {
        if (node == null) return;
        String indent = "  ".repeat(level);
        System.out.println(indent + prefix + "Spot ID: " + node.spotID);

        if (node.left != null || node.right != null) {
            if (node.left != null) {
                printTreeRecursive(node.left, level + 1, "L-> ");
            } else {
                System.out.println(indent + "  " + "L-> null");
            }

            if (node.right != null) {
                printTreeRecursive(node.right, level + 1, "R-> ");
            } else {
                System.out.println(indent + "  " + "R-> null");
            }
        }
    }
}
