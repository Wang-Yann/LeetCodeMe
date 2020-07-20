#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-08 22:35:03
# @Last Modified : 2020-05-08 22:35:03
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
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
#  返回：
#
#  [3,9,20,15,7]
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
#  👍 27 👎 0

import collections
from typing import List

import pytest

from common_utils import TreeNode


class Solution:

    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


@pytest.mark.parametrize("args,expected", [
    (TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),
     [3, 9, 20, 15, 7]),
])
def test_solutions(args, expected):
    assert Solution().levelOrder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
