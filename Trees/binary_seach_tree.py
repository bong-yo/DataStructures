import sys
from utils import Paths
from typing import List
sys.path.append(Paths.QUEUE_DIR)
from my_queue import Queue


class Node:
    def __init__(self, key, attributes=[]):
        self.key = key
        self.attr = attributes
        self.left = None
        self.right = None


class BinarySearchTree():
    '''
    All elements of left subtree are smallet than node.
    All elements of right subtree are bigger than node.
    Same value go to RIGHT child (by pure choice).
    '''
    def __init__(self, values: List[int]):
        super(BinarySearchTree, self).__init__()
        self.root = None
        for v in values:
            self.insert(v)

    def insert(self, value: int) -> bool:
        def _insert(node: Node, root: Node) -> bool:
            if node.key < root.key:  # Descend tree to left child.
                if root.left is None:
                    root.left = node
                    return True
                else:
                    _insert(node, root.left)
            elif node.key > root.key:  # Descend tree to right child.
                if root.right is None:
                    root.right = node
                    return True
                else:
                    _insert(node, root.right)
            return False  # Value is already in the tree.

        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        return _insert(node, self.root)

    def delete(self, key, root: Node = "root") -> None:
        if root == "root":
            root = self.root

        elif root is None:
            return False

        if key < root.key:
            self.delete(key, root.left)

        elif key > root.key:
            self.delete(key, root.right)

        elif key == root.key:
            # Get rightmost (biggest) child of the left (smallest) subtree.
            rm_child, rm_parent = self.get_rightmost_child(root.left)
            rm_parent.right = rm_child.left
            root.key = rm_child.key
            return True

    def get_leftmost_child(self, node: Node) -> Node:
        parent = None
        while node.left:
            parent = node
            node = node.left
        return node, parent

    def get_rightmost_child(self, node: Node) -> Node:
        parent = None
        while node.right:
            parent = node
            node = node.right
        return node, parent

    def depth(self, node: Node = "root"):
        if node == "root":  # Always start from root.
            node = self.root
        return 1 + max(self.depth(node.left), self.depth(node.right)) \
            if node is not None else 0

    def traverse_inorder(self, node: Node = "root"):
        if node == "root":  # Always start from root.
            node = self.root
        elif node is None:  # End of tree reached.
            return
        self.traverse_inorder(node.left)
        print(node.key)
        self.traverse_inorder(node.right)

    def traverse_preorder(self, node: Node = "root"):
        if node == "root":  # Always start from root.
            node = self.root
        elif node is None:  # End of tree reached.
            return
        print(node.key)
        self.traverse_inorder(node.left)
        self.traverse_inorder(node.right)

    def traverse_postorder(self, node: Node = "root"):
        if node == "root":  # Always start from root.
            node = self.root
        elif node is None:  # End of tree reached.
            return
        self.traverse_inorder(node.left)
        self.traverse_inorder(node.right)
        print(node.key)

    def trasverse_levelorder(self):
        levels = [[]]
        q = Queue()
        q.enqueue({"node": self.root, "level": 0})
        while not q.queue_empty():
            x = q.dequeue()
            # Save node to appropriate level.
            if x["level"] == len(levels):  # Create new level.
                levels.append([x["node"].key])
            else:  # Save to existing level.
                levels[x["level"]].append(x["node"].key)
            # Proceed with the queue.
            if x["node"].left is not None:
                q.enqueue({"node": x["node"].left, "level": x["level"] + 1})
            if x["node"].right is not None:
                q.enqueue({"node": x["node"].right, "level": x["level"] + 1})
        return levels

    def Morris_inorder(self):
        """Morris algo. for tree traversal with O(1) space complexity."""
        root = self.root
        while root:
            if not root.left:
                yield root.key
                root = root.right
            else:
                # Find root predecessor (i.e. rightmost child of root's left child)
                pre = root.left
                while pre.right and not pre.right == root:
                    pre = pre.right
                if not pre.right:  # If the link doesn't exist yet: make root the right child of its inorder predecessor.
                    pre.right = root
                    root = root.left  # Move root to left child.
                else:  # The left subtree of root has been completely traversed already.
                    yield root.key
                    root = root.right

    def __str__(self):
        return "\n".join(str(level) for level in self.trasverse_levelorder())


if __name__ == "__main__":
    bst = BinarySearchTree([17, 3, 15, 10, 3245, 3, 2, 56, 24, 7, 234, 14, 2, 1, 6, 3])
    print(bst)
    print()
    print([x for x in bst.Morris_inorder()])