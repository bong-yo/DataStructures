from typing import Dict


class Node:
    def __init__(self):
        self.children: Dict[str, Node] = {}
        self.word: str = None


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def search(self, word: str) -> bool:
        node = self._get_node(word)
        if not node or not node.word:  # 'word' is saved in the Trie as a word and not as a substring of a larger word.
            return False
        return True

    def insert(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        if node.word:  # word is in the Trie already.
            return False
        node.word = word
        return True

    def delete(self, word: str) -> bool:
        node = self._get_node(word)
        if not node or not node.word:  # 'word' not in the Trie.
            return False
        node.word = None

        def _delete(node: Node, word: str, i: int) -> bool:
            """Recursively delete all nodes that ONLY belong to 'word'"""
            if i == len(word) - 1 and not node.children:
                return True
            c = word[i]
            if _delete(node.children[c], word, i + 1):
                del node.children[c]
            return not node.word and not node.children

        return True

    def _get_node(self, word: str) -> Node():
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def print_vocab(self, node: Node = "root"):
        if node == "root":
            node = self.root
        if node.word:
            print(node.word)
        for _, child_node in node.children.items():
            self.print_vocab(child_node)


if __name__ == "__main__":
    trie = Trie()
    print(trie.insert("the"))
    print(trie.insert("there"))
    print(trie.insert("house"))
    print(trie.search("hound"))
    print(trie.search("the"))
    print(trie.insert("hou"))
    print(trie.insert("house"))
    print()
    trie.print_vocab()
    trie.delete("the")
    print()
    trie.print_vocab()
    trie.delete("house")
    print()
    trie.print_vocab()
