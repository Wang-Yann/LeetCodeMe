#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 14:52:45
# @Last Modified : 2020-04-07 14:52:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def init_list_from_str(cls, s):
        """1->2->3->4->5 """
        if not s:
            return None
        node_list = [cls(int(x.strip())) for x in s.split("->")]
        for i in range(0, len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        return node_list[0]

    @classmethod
    def initList(cls, data):
        if not data:
            return None
        head = cls(data[0])
        r = head
        p = head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

    def __lt__(self, other):
        if not (self and other):
            return False
        return self.val < other.val


class TrieNode(object):
    """
    前缀树
    """

    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True

    def __repr__(self):
        return "TrieNode[{}]{} ".format("->".join(self.leaves.keys()), self.is_string)


class Node:

    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    @classmethod
    def initList(cls, data):

        if not data:
            return None
        node_list = []
        for node_val, rand in data:
            node_list.append(cls(node_val))
        length = len(data)
        for idx in range(length):
            if idx < length - 1:
                node_list[idx].next = node_list[idx + 1]
            rand = data[idx][1]
            if rand is not None:
                node_list[idx].random = node_list[rand]
        return node_list[0]

    def __repr__(self):
        if self:
            return "{}[>{}] -> {}".format(self.val, self.random.val if self.random else None,
                                          repr(self.next))


class DoubleListNode:

    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

    def __repr__(self):
        if self:
            return "{} <=> {}".format(self.val, repr(self.next))

    def __lt__(self, other):
        if not (self and other):
            return False
        return self.val < other.val


class DoubleWithChildNode:

    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    @classmethod
    def initList(cls, list_list):

        if not list_list:
            return None
        node_dict = collections.defaultdict(lambda:cls(None))
        m, n = len(list_list), len(list_list[0])
        for i in range(m):
            length_row = len(list_list[i])
            for j in range(length_row):
                val = list_list[i][j]
                if val is not None:
                    node_dict[(i, j)] = cls(val)

        for i in range(m):
            length_row = len(list_list[i])
            for j in range(length_row):
                val = list_list[i][j]
                if val is None:
                    continue
                if 0 < j < length_row - 1:
                    node_dict[(i, j)].prev = node_dict[(i, j - 1)]
                    node_dict[(i, j)].next = node_dict[(i, j + 1)]
                elif j == 0:
                    node_dict[(i, j)].next = node_dict[(i, j + 1)]
                elif j == length_row - 1:
                    node_dict[(i, j)].prev = node_dict[(i, j - 1)]
        for i in range(1, m):
            length_row = len(list_list[i])
            for idx in range(length_row):
                val = list_list[i][idx]
                if val is not None:
                    node_dict[(i - 1, idx)].child = node_dict[(i, idx)]
                    break

        return node_dict[(0, 0)]

    def __repr__(self):
        if self:
            res = """{} <=> {} """.format(self.val, repr(self.next))
            if self.child:
                res += "[Child]{}".format(repr(self.child))
            return res


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class UnionFind:

    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * m * n
        self.rank = [0] * m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        """make sure rank(root_x)>=rank(root_y)"""
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
            self.count -= 1

    def getCout(self):
        return self.count


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None

    @classmethod
    def initTreeSimple(cls, data, relations_l, relations_r):

        if not data:
            return []
        node_list = []
        for node_val in data:
            if node_val is not None:
                node_list.append(cls(node_val))
            else:
                node_list.append(None)
        for root_idx, l_idx in relations_l:
            node_list[root_idx].left = node_list[l_idx]
        for root_idx, r_idx in relations_r:
            node_list[root_idx].right = node_list[r_idx]
        return node_list[0]

    def __lt__(self, other):
        if not (self and other):
            return False
        return self.val < other.val
