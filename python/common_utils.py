#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-07 14:52:45
# @Last Modified : 2020-04-07 14:52:45
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import collections
import os
import psutil
import resource

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


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
            return "{} -> {}".format(str(self.val), repr(self.next))

    def __lt__(self, other):
        if not (self and other):
            return False
        return self.val < other.val

    @classmethod
    def reverseList(cls, head):
        """
        TODO 示范写法
        """
        dummy = ListNode(-1)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    @classmethod
    def reverseListRec(cls, head):
        """
         示范写法
        """
        if head.next is None:
            return head
        last = cls.reverseListRec(head.next)
        head.next.next = last
        head.next = None
        return


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
        node_dict = collections.defaultdict(lambda: cls(None))
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


class TreeNodeWithNext:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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


class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))

    def find(self, x):
        if self.set[x] != x:
            self.set[x] = self.find(self.set[x])
        return self.set[x]

    def find_set(self, x):
        return self.find(x)

    def union_set(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        return True


class TreeNode:

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(str(cur.val))
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

    @classmethod
    def initPreOrder(cls, data_list):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rebuild(l):
            val = l.pop(0)
            if val is None:
                return None
            root = TreeNode(val)
            root.left = rebuild(l)
            root.right = rebuild(l)
            return root

        return rebuild(data_list)


class TreeNodeWithChildren:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

    def __repr__(self):
        if self:
            if self.children:
                return "{}[{}]".format(self.val, [repr(x) for x in self.children])
            else:
                return "{}[]".format(self.val)


class NestedInteger:

    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.value = value or []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.value, int)

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if not self.isInteger():
            self.value.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return int(self.value)

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return self.value

    def __repr__(self):
        if self:
            return "{}".format(repr(self.value))


class UndirectedGraphNode:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []

    def __repr__(self):
        if self:
            return "{}<=>[{}]".format(self.val, repr(self.neighbors))


class Interval:

    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __str__(self):
        return "{}->{}".format(self.start, self.end)

    __repr__ = __str__


def memory_limit(max_mem):
    def decorator(f):
        def wrapper(*args, **kwargs):
            process = psutil.Process(os.getpid())
            prev_limits = resource.getrlimit(resource.RLIMIT_AS)
            resource.setrlimit(resource.RLIMIT_AS, (process.memory_info().rss + max_mem, -1))
            result = f(*args, **kwargs)
            resource.setrlimit(resource.RLIMIT_AS, prev_limits)
            return result

        return wrapper

    return decorator
