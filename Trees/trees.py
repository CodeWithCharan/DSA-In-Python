#General tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.childern = []

    def add_child(self, child):
        child.parent = self
        self.childern.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    laptops.add_child(TreeNode("MAC"))
    laptops.add_child(TreeNode("WINDOWS"))
    laptops.add_child(TreeNode("LINUX"))

    cell = TreeNode("Cell Phones")
    cell.add_child(TreeNode("iPhone"))
    cell.add_child(TreeNode("Android"))
    cell.add_child(TreeNode("Google pixel"))
    
    tv = TreeNode("TV")
    tv.add_child(TreeNode("samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptops)
    root.add_child(cell)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()