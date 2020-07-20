#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-09 22:47:36
# @Last Modified : 2020-05-09 22:47:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
#
#
#
#  为了让您更好地理解问题，以下面的二叉搜索树为例：
#
#
#
#
#
#
#
#  我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是
# 第一个节点。
#
#  下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
#
#
#
#
#
#
#
#  特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
#
#
#
#  注意：本题与主站 426 题相同：https://leetcode-cn.com/problems/convert-binary-search-tree-
# to-sorted-doubly-linked-list/
#
#  注意：此题对比原题有改动。
#  Related Topics 分治算法
#  👍 70 👎 0


import pytest

from common_utils import TreeNode as Node


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        """
        https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
        solution/mian-shi-ti-36-er-cha-sou-suo-shu-yu-shuang-xian-5/
        画图
        """
        self.pre = None
        self.head = None

        def dfs(cur):
            if not cur:
                return None
            dfs(cur.left)
            if self.pre:
                # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else:
                # 记录头节点
                self.head = cur
            self.pre = cur
            dfs(cur.right)

        if not root:
            return None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
