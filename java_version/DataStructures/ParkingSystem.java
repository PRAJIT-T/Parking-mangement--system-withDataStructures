package DataStructures;

public class ParkingSystem {
    private Tree tree;
    private CustomLinkedList queue = new CustomLinkedList();
    private int currentSize = 0;
    private int maxSize;
    private int occupancyPercentage;
    // Tree type constants
    public static final int BST = 0;
    public static final int AVL = 1;
    
    /*
    public ParkingSystem(int n) {
        this(n, BST); // Default to BST
    }
    */
    public ParkingSystem(int n, int treeType) {
        this.maxSize = n;

        switch (treeType) {
            case AVL:
                tree = new AVLTree();
                ((AVLTree)tree).createTree(n);
                break;
            default: // BST
                tree = new BinarySearchTree();
                ((BinarySearchTree)tree).createTree(n);
                break;
        }
    }

    public int addCar(String RegNo) {
        if(this.queue.head != null){
            Node QueueNode = this.queue.head;
            while(QueueNode != null){
                if(QueueNode.regNo.equals(RegNo)){
                    return QueueNode.spotID;
                }
                QueueNode = QueueNode.right;
            }
        }
        if(this.currentSize >= this.maxSize){
            System.out.println("Parking is full. Cannot add more cars.");
            return -1;
        }
        Node node = tree.removeSpot(tree.searchForFreeSpot());
        queue.enqueue(node);
        node.setRegNo(RegNo);
        currentSize++;
        updateStatus();
        int a = this.queue.printLastSpotID();
        return a;
    }

    public boolean removeCar(String RegNo) {
        Node node = queue.findAndPop(RegNo);
        if (node != null) {
            node.setRegNo(null);
            tree.insertSpot(node);
            currentSize--;
            updateStatus();
            return true;
        } else {
            System.out.println("Car with registration number " + RegNo + " not found.");
            return false;
        }
    }
    
    public void printTree() {
        tree.printTree();
    }
    
    public void printQueue() {
        queue.printQueue();
    }

    private void updateStatus(){
        occupancyPercentage = (int) ((currentSize / (double) maxSize) * 100);
    }   
    
    public String getOccupancyStatus() {
        return "Occupancy: " + currentSize + "/" + maxSize;
    }

    public int printLastSpotID() {
        return this.queue.printLastSpotID();
    }

    public int getOccupancyPercentage() {
        return occupancyPercentage;
    }
    
    /**
     * Returns the total number of parking spots in the system
     * @return total number of spots
     */
    
    public int getTotalSpots() {
        return maxSize;
    }

    /**
     * Returns the number of currently occupied spots
     * @return number of occupied spots
     */
    public int getOccupiedSpots() {
        return currentSize;
    }
}
