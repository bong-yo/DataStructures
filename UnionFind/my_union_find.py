from typing import List
from collections import defaultdict


class Element:
    def __init__(self, name, attr: List = []):
        self.name = name
        self.attributes = attr


class UnionFind:
    def __init__(self, elements: List[Element] = []):
        self.element_group = {}  # Map each element to its current group.
        self.group_elements = defaultdict(list)  # List of elements in a group.

    def merge(self, elem1: Element, elem2: Element):
        if not self.exists(elem1) or not self.exists(elem2):
            return False

        group1, size1 = self.get_group(elem1)
        group2, size2 = self.get_group(elem2)

        if group1 != group2:
            if size1 >= size2:
                self.change(group2, group1)
            else:
                self.change(group1, group2)
            return True
        else:
            return False

    def change(self, group1: int, group2: int):
        '''Assign elements in group1 to group2'''
        for elem in self.group_elements[group1]:
            self.element_group[elem.name] = group2
            self.group_elements[group2].append(elem)
        self.group_elements.pop(group1)

    def insert(self, elem: Element, group: int):
        self.element_group[elem.name] = group
        self.group_elements[group].append(elem)

    def exists(self, elem: Element):
        return elem.name in self.element_group

    def find(self, elem: Element):
        if self.exists(elem):
            return self.element_group[elem.name]
        else:
            return None

    def get_group(self, elem: Element):
        group_name = self.find(elem)
        group_size = len(self.group_elements.get(group_name, []))
        return group_name, group_size
