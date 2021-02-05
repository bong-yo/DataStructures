from binary_seach_tree import BinarySearchTree, Node

bst = BinarySearchTree()
bst.insert(Node(1))
bst.insert(Node(3))
bst.insert(Node(6))
bst.insert(Node(2))
bst.insert(Node(7))
bst.insert(Node(3))
bst.insert(Node(4))
bst.insert(Node(3))
bst.insert(Node(3))
print(bst)
print(bst.depth())
bst.delete(6)
print(bst)
print(bst.depth())
print(0)
