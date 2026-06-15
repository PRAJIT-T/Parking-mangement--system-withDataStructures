class Node:
    def __init__(self, number):
        self.spot_id = number
        self.parent = None
        self.left = None
        self.right = None
        self.reg_no = None
        self.height = 0  # Added height attribute for AVL tree
    
    def set_reg_no(self, reg_no):
        self.reg_no = reg_no
