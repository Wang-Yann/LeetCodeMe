#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-08 22:35:03
# @Last Modified : 2020-05-08 22:35:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
#
#
#  例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层次遍历结果：
#
#  [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
#
#
#
#  提示：
#
#
#  节点总数 <= 1000
#
#  Related Topics 树 广度优先搜索
#  👍 32 👎 0




import traceback
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res =[]
        q=collections.deque([root])
        level =0
        while q:
            length = len(q)
            res.append([])
            for i in range(length):
                node =q.popleft()
                if level%2:
                    res[level].insert(0,node.val)
                else:
                    res[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return res

@pytest.mark.parametrize("args,expected", [
    (TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7))),
     [[3], [20,9], [15,7]]),
])
def test_solutions(args, expected):
    assert Solution().levelOrder(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])


