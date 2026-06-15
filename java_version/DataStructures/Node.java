package DataStructures;

public class Node {
    int spotID;
    Node parent, left, right;
    String regNo;
    int height; // Added height attribute for AVL tree

    Node(int number) {
        this.spotID = number;
        this.parent = this.left = this.right = null;
        this.regNo = null;
        this.height = 0; // Initialize height to 0
    }

    protected void setRegNo(String regNo) {
        this.regNo = regNo;
    }
}