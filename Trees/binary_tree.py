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
                # val is in right of right subtree
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
    
    def find_min(self):
        if self.left == None:
            # if there is no left subtree to the current node i.e., self.data
            return self.data
        else:
            # if there is left subtree to the current node
            return self.left.find_min()
        
    def find_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.find_max()
        
        
    
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

    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 1]
    build_num_tree = build_tree(numbers)

    print("\nIn order traversal: ", build_num_tree.in_order())
    print("Pre order traversal: ", build_num_tree.pre_order())
    print("Post order traversal: ", build_num_tree.post_order())

    print(build_num_tree.search(17)) # Search for the element and give output True or Flase

    print("Sum of elements: ",sum(set(numbers))) # here set() function removes duplicate elements i.e., 1 repeated two times

    print("Maximum value in tree: ", build_num_tree.find_max()) # returns maximum value
    print("Minumum value in tree: ", build_num_tree.find_min()) # returns minimum value