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
    
    def search(self, val):
        if self.data == val:
            # val is the root node
            return True
        
        if val < self.data:
            # val is in left subtree
            if self.left:
                # val is in left subtree of left subtree
                return self.left.search(val)
            else:
                # val doesn't exist in the tree
                return False
            
        else:
            # val is in right subtree
            if self.right:
                # val is in left subtree of left subtree
                return self.right.search(val)
            else:
                # val doesn't exist in the tree
                return False

    
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
    
    def pre_order(self):
        elements = []

        # Root
        elements.append(self.data)

        # Left Subtree
        if self.left:
            elements += self.left.pre_order()

        # Right Subtree
        if self.right:
            elements += self.right.pre_order()
            
        return elements
    
    def post_order(self):
        elements = []

        # Left Subtree
        if self.left:
            elements += self.left.post_order()

        # Right Subtree
        if self.right:
            elements += self.right.post_order()

        # Root
        elements.append(self.data)

        return elements
    
def build_tree(elements):
    print("Elements in the list: ", elements)
    root = BinaryTreeNode(elements[0]) # added root node

    for i in range(1, len(elements)):
        root.add_child(elements[i]) # added child nodes
    return root

if __name__ == '__main__':
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # countries_build_tree = build_tree(countries)

    # print("In order traversal: ", countries_build_tree.in_order())

    # print(countries_build_tree.search("USA"))

    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    build_num_tree = build_tree(numbers)

    print("\nIn order traversal: ", build_num_tree.in_order())
    print("Pre order traversal: ", build_num_tree.pre_order())
    print("Post order traversal: ", build_num_tree.post_order())

    # print(build_num_tree.search(17))