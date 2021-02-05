import sys
from utils import Paths
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
    def __init__(self, root: Node = None):
        super(BinarySearchTree, self).__init__()
        self.root = root

    def insert(self, node: Node, current: Node = 'root'):
        if self.root is None:
            self.root = node

        elif current == "root":
            self.insert(node, self.root)

        elif current is None:  # End of tree reached -> save node as a leaf.
            current = node

        elif node.key < current.key:  # Descend tree to left child.
            if current.left is None:
                current.left = node
            else:
                self.insert(node, current.left)

        elif node.key >= current.key:  # Descend tree to right child.
            if current.right is None:
                current.right = node
            else:
                self.insert(node, current.right)

        else:
            print("Something wrong happened!")

    def delete(self, key, current: Node = "root") -> None:
        if current == "root":
            current = self.root

        elif current is None:
            return False

        if key < current.key:
            self.delete(key, current.left)

        elif key > current.key:
            self.delete(key, current.right)

        elif key == current.key:
            # Get rightmost (biggest) child of the left (smallest) subtree.
            rm_child, rm_parent = self.get_rightmost_child(current.left)
            rm_parent.right = rm_child.left
            current.key = rm_child.key
            return True

    def get_leftmost_child(self, node: Node) -> Node:
        while node.left is not None:
            parent = node
            node = node.left
        return node, parent

    def get_rightmost_child(self, node: Node) -> Node:
        while node.right is not None:
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

    def __str__(self):
        return "\n".join(str(level) for level in self.trasverse_levelorder())
