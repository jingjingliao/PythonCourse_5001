class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"({self.value}, {self.left}, {self.right})"


class BinaryTree:
    def __init__(self, val):
        self.root = Node(val)

    def __str__(self):
        return "BinTree( {} )".format(str(self.root))

    def add_val_l(self, val):
        n = Node(val)
        self.add_node_l(self.root, n)

    def add_node_l(self, current_node, new_node):
        if current_node.left is None:
            current_node.left = new_node
        elif current_node.right is None:
            current_node.right = new_node
        else:
            self.add_node_l(current_node.left, new_node)

    def add_val_r(self, val):
        n = Node(val)
        self.add_node_r(self.root, n)

    def add_node_r(self, current_node, new_node):
        if current_node.right is None:
            current_node.right = new_node
        elif current_node.right is None:
            current_node.right = new_node
        else:
            self.add_node_r(current_node.right, new_node)

    def contains(self, value):
        return self.contains_node(self.root, value)

    def contains_node(self, node, value):
        if node.value == value:
            return True
        else:
            if node.left:
                if self.contains_node(node.left, value):
                    return True
            if node.right:
                if self.contains_node(node.right, value):
                    return True
        return False


bintree = BinaryTree("A")
bintree.add_val_l("B")
bintree.add_val_l("C")
bintree.add_val_r("G")
bintree.add_val_r("H")
bintree.add_val_l("D")
bintree.add_val_l("E")
bintree.add_val_r("I")
bintree.add_val_l("F")
print(bintree)
