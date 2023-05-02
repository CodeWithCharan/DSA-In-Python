# Exercise 1

#General tree
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
    
    def print_tree(self, property_name):
        if property_name == "both":
            value = self.name + '(' + self.designation + ')'
        elif property_name == "name":
            value = self.name
        else:
            value = self.designation

        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.childern:
            for child in self.childern:
                child.print_tree(property_name)

def build_product_tree():
    root = TreeNode("Nilupul","CEO")

    CTO = TreeNode("Chinmay","CTO")
    IH = TreeNode("Vishwa","Infrastructure Head")
    CTO.add_child(IH)
    IH.add_child(TreeNode("Dhaval","Cloud Manager"))
    IH.add_child(TreeNode("Abhijit","App Manager"))

    CTO.add_child(TreeNode("Aamir","Application Head"))

    HR = TreeNode("Gels","HR Head")
    HR.add_child(TreeNode("Peter","Recruitment Manager"))
    HR.add_child(TreeNode("Wagas","Policy Manager"))

    root.add_child(CTO)
    root.add_child(HR)

    return root

if __name__ == '__main__':
    root_node = build_product_tree()
    root_node.print_tree("name")
    print("_____________________________")
    root_node.print_tree("designation")
    print("_____________________________")
    root_node.print_tree("both")