#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 14:52:45
# @Last Modified : 2020-04-07 14:52:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


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
