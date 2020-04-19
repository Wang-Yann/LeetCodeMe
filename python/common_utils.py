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
            return "{}[>{}] -> {}".format(self.val, self.random.val if self.random else None, repr(self.next))


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
