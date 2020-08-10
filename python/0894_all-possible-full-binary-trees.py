#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-24 22:19:36
# @Last Modified : 2020-04-24 22:19:36
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
#
#  返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
#
#  答案中每个树的每个结点都必须有 node.val=0。
#
#  你可以按任何顺序返回树的最终列表。
#
#
#
#  示例：
#
#  输入：7
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0
# ,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
#
#
#
#
#
#  提示：
#
#
#  1 <= N <= 20
#
#  Related Topics 树 递归
#  👍 127 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution:

    def __init__(self):
        self.possible_map = {1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []

        if N not in self.possible_map:
            results = []
            for i in range(N):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        node = TreeNode(0)
                        node.left = left
                        node.right = right
                        results.append(node)
            self.possible_map[N] = results

        return self.possible_map[N]


@pytest.mark.parametrize("kw,expected", [
    (dict(N=7), [['0', '0', '0', '#', '#', '0', '0', '#', '#', '0', '0'],
                 ['0', '0', '0', '#', '#', '0', '0', '0', '0'],
                 ['0', '0', '0', '0', '0', '0', '0'],
                 ['0', '0', '0', '0', '0', '#', '#', '#', '#', '0', '0'],
                 ['0', '0', '0', '0', '0', '#', '#', '0', '0']]),
])
def test_solutions(kw, expected):
    assert repr(Solution().allPossibleFBT(**kw)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
