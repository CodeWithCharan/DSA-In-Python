#Exercise 2
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
    
    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree(level)

def build_location_tree():
    root = TreeNode("Global")

    Country = TreeNode("India")
    Guj = TreeNode("Gujarat")
    Kar = TreeNode("Karnataka")
    Country.add_child(Guj)
    Country.add_child(Kar)
    Guj.add_child(TreeNode("Ahmedabad"))
    Guj.add_child(TreeNode("Baroda"))

    Kar.add_child(TreeNode("Bangluru"))
    Kar.add_child(TreeNode("Mysore"))

    Country2 = TreeNode("USA")
    NJ = TreeNode("New Jersey")
    CF = TreeNode("California")
    Country2.add_child(NJ)
    Country2.add_child(CF)
    NJ.add_child(TreeNode("Princeton"))
    NJ.add_child(TreeNode("Trenton"))

    CF.add_child(TreeNode("San Fancisco"))
    CF.add_child(TreeNode("Mountain view"))
    CF.add_child(TreeNode("Palo Alto"))
    
    root.add_child(Country)
    root.add_child(Country2)

    print("\nFor level 1")
    root.print_tree(1)
    print("_"*10)
    print("\nFor level 2")
    root.print_tree(2)
    print("_"*10)
    print("\nFor level 3")
    root.print_tree(3)

if __name__ == '__main__':
    build_location_tree()

    