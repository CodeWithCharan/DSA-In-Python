class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return # It will remove duplicate values
        
        if data < self.data:
            # Left Subtree
            if self.left:
                # If it is a left subtree of left subtree
                self.left.add_child(data)
            else:
                # If it is left subtree of root node
                self.left = BinaryTreeNode(data)
        else:
            # Right Subtree
            if self.right:
                # If it is a right subtree of right subtree
                self.right.add_child(data)
            else:
                # If it is right subtree of root node
                self.right = BinaryTreeNode(data)

    def in_order(self):
        elements = []

        # Left Subtree
        if self.left:
            elements += self.left.in_order()

        # Root
        elements.append(self.data)

        # Right Subtree
        if self.right:
            elements += self.right.in_order()
            
        return elements
       
    def find_min(self):
        if self.left == None:
            # if there is no left subtree to the current node i.e., self.data
            return self.data
        else:
            # if there is left subtree to the current node
            return self.left.find_min()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # for "no child"
            if self.left is None and self.right is None:
                return None
            
            # for "one child"
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            # for "two child" we will choose minimum value from right sub-tree and replace it with current node
            mini_val = self.right.find_min()
            self.data = mini_val
            self.right = self.right.delete(mini_val)
        return self
            
def build_tree(elements):
    print("Elements in the list: ", elements)
    root = BinaryTreeNode(elements[0]) # added root node

    for i in range(1, len(elements)):
        root.add_child(elements[i]) # added child nodes
    return root

if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    build_num_tree = build_tree(numbers)

    print("\nBefore:\nIn order traversal: ", build_num_tree.in_order())
    
    build_num_tree.delete(20)
    print("\nAfter:\nIn order traversal: ", build_num_tree.in_order())