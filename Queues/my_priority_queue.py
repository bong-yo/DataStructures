class Node:
    def __init__(self, value, attributes):
        self.value = value
        self.attributes = attributes


class Heap:
    def __init__(self, root: Node = None):
        self.tree = {0: root}
        self.n_nodes = 0

    def enqueue(self, node: Node) -> None:
        if self.tree[0] is None:
            self.tree[0] = node
        else:
            new_node_pos = len(self.tree)
            self.tree[new_node_pos] = node  # Insert node at the end of the tree.
            self.bubble_up(new_node_pos)  # Bubble up to right position in the tree.

    def dequeue(self) -> Node:
        if len(self.tree) == 0:
            return None

        root = self.tree[0]  # Get root.
        self.swap_with_last_node(position=0)  # Copy last node to the root & remove last node.
        self.bubble_down(node_pos=0)  # Bubble down to the right position in the tree.
        return root

    def bubble_up(self, node_pos) -> None:
        '''Iteratively compare node with parent and swap if bigger'''
        parent_pos = self.get_parent_position(node_pos)
        node_value = self.tree[node_pos].value
        while node_value < self.tree[parent_pos].value:
            self.swap(node_pos, parent_pos)
            node_pos = parent_pos
            if node_pos > 0:
                parent_pos = self.get_parent_position(node_pos)
            else:
                break

    def bubble_down(self, node_pos: int) -> None:
        '''Iteratively compare node with biggest child and swap if smaller'''
        child_pos = self.get_smallest_child_position(node_pos)
        while child_pos is not None:
            self.swap(node_pos, child_pos)
            node_pos = child_pos
            child_pos = self.get_smallest_child_position(node_pos)

    def swap(self, pos1: int, pos2: int) -> None:
        node1 = self.tree[pos1]
        self.tree[pos1] = self.tree[pos2]
        self.tree[pos2] = node1

    def swap_with_last_node(self, position: int) -> None:
        if len(self.tree) > 1:
            self.tree[position] = self.tree.pop(len(self.tree) - 1)
        else:
            self.tree.pop(0)

    def get_child_pos(self, position: int, child_type: str):
        child_pos = 2 * position + 1 + int(child_type == 'right')
        return child_pos if child_pos < len(self.tree) else None

    def get_parent_position(self, position: int) -> int:
        parent_pos = (position - 1) // 2
        return parent_pos

    def get_smallest_child_position(self, position: int) -> int:
        child_l_pos = self.get_child_pos(position, 'left')
        child_r_pos = self.get_child_pos(position, 'right')

        if child_r_pos is None:
            if child_l_pos is None:
                return None
            else:
                return child_l_pos
        elif self.tree[child_l_pos].value < self.tree[child_r_pos].value:
            return child_l_pos
        else:
            return child_r_pos


if __name__ == "__main__":
    heap = Heap()
    heap.enqueue(Node(19, (1, 4)))
    heap.enqueue(Node(12, (0, 7)))
    heap.enqueue(Node(29, (2, 3)))
    heap.enqueue(Node(17, (3, 9)))
    element = heap.dequeue()
    element = heap.dequeue()
    element = heap.dequeue()
    element = heap.dequeue()
    element = heap.dequeue()
    element = heap.dequeue()
    element = heap.dequeue()
    print(element)
