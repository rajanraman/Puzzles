class BinaryTree:
    def __init__(self,root):
        self.key = root
        self.left_child = None
        self.right_child = None
    
    def insert_left(self,new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_right_child(self):
        return self.right_child
    def get_left_child(self):
        return self.left_child
    def get_root_val(self):
        return self.key
    def set_root_val(self,obj):
        self.key = obj

max_val = 0
def find_max(btree):
    global max_val
    max_val = btree.get_root_val()
    if btree.get_left_child() is not None:
        max_val = max(max_val,find_max(btree.get_left_child()))
    if btree.get_right_child() is not None:
        max_val = max(max_val,find_max(btree.get_right_child()))
    return max_val
