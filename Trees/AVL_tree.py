"""
Implementation of self-balancing AVL Tree.
"""
import sys
from copy import deepcopy


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.bf = 0

class AVL_Tree:
    def __init__(self, root: TreeNode = None):
        self.root = root

    def insert(self, node: TreeNode, root: TreeNode = 'root') -> bool:
        if not self.root:
            self.root = node
            return True

        if root == 'root':
            root = self.root

        if node.val > root.val:
            if root.right:
                self.insert(node, root.right)
            else:
                root.right = node
        elif node.val < root.val:
            if root.left:
                self.insert(node, root.left)
            else:
                root.left = node
        else:  # if it hits here means the value is alredy in the tree.
            return False

        self.update(root)
        return self.balance(root)
    
    def delete(self, node: TreeNode, root: TreeNode = "root") -> bool:
        if not root:
            return False

        if root == "root":
            root = self.root
        
        if node.val > root.val:
            self.delete(node, root.right)
        elif node.val < root.val:
            self.delte(node, root.left)
        else:
            root = None

        return True

    def update(self, root: TreeNode) -> None:
        '''
        Update node hight and balance factor.
        By convention hight of a leaf node = 0.
        '''
        lh = self.height(root.left)
        rh = self.height(root.right)
        root.height = 1 + max(lh, rh)
        root.bf = lh - rh

    def balance(self, root: TreeNode) -> bool:
        '''
        If root-subtree is :
        - unbalanced to the left (bf == 2) -> rotate right
        - unbalanced to the right (bf == -2)-> rotate left
        - balanced (bf in [-1, 0, 1]) -> do nothing
        '''
        assert(abs(root.bf) <= 2)
        if root.bf == 2:
            # Completely left unbalanced -> only 1 right rotation.
            if root.left.bf == 1:
                print("R")
                self.rotate_right(root)
            # Left-right unbalanced -> 1 left anf 1 right rotation.
            elif root.left.bf == -1:
                print("LR")
                self.rotate_left(root.left)
                self.rotate_right(root)
            else:
                sys.exit("Error! the tree is unbalanced!")

        elif root.bf == -2:
            # Completely right unbalanced -> only 1 left rotation.
            if root.right.bf == -1:
                print("L")
                self.rotate_left(root)
            # Right-left unbalanced -> 1 right anf 1 left rotation.
            elif root.right.bf == 1:
                print("RL")
                self.rotate_right(root.right)
                self.rotate_left(root)

        return True

    def height(self, node: TreeNode) -> int:
        return -1 if not node else node.height

    def rotate_left(self, root: TreeNode) -> TreeNode:
        child_right = root.right
        root.right = child_right.left
        child_right.left = deepcopy(root)
        root.val = child_right.val
        root.right = child_right.right
        root.left = child_right.left
        self.update(child_right.left)
        self.update(child_right)

    def rotate_right(self, root: TreeNode) -> None:
        child_left = root.left
        root.left = child_left.right
        child_left.right = deepcopy(root)
        root.val = child_left.val
        root.right = child_left.right
        root.left = child_left.left
        self.update(root.right)
        self.update(root)

    def print_levelorder(self) -> None:
        queue = [(self.root, 0)]
        levels = [[]]
        while queue:
            x, level = queue.pop(0)
            if level == len(levels):
                levels.append([])
            levels[level].append(x)
            if x:
                queue.append((x.left, level + 1))
                queue.append((x.right, level + 1))
        # Print levels (last level ia always all Nones).
        for lev in levels[:-1]:
            print([None if not x else x.val for x in lev])


if __name__ == "__main__":
    avlt = AVL_Tree()
    avlt.insert(TreeNode(4))
    avlt.print_levelorder()
    print()
    avlt.insert(TreeNode(1))
    avlt.print_levelorder()
    print()
    avlt.insert(TreeNode(14))
    avlt.print_levelorder()
    print()
    avlt.insert(TreeNode(3))
    avlt.print_levelorder()
    print()
    avlt.insert(TreeNode(7))
    avlt.print_levelorder()
    print()
    avlt.insert(TreeNode(5))
    avlt.print_levelorder()
    print()
    avlt.insert(TreeNode(2))
    avlt.print_levelorder()
