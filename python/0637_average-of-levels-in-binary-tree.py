#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-23 22:48:32
# @Last Modified : 2020-04-23 22:48:32
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
#
#
#
#  示例 1：
#
#  输入：
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 输出：[3, 14.5, 11]
# 解释：
# 第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
#
#
#
#
#  提示：
#
#
#  节点值的范围在32位有符号整数范围内。
#
#  Related Topics 树
#  👍 136 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution:

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        if not root:
            return ans
        queue = [root]
        while queue:
            length = len(queue)
            sum = 0
            for i in range(length):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(sum / length)
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))), [3.0, 14.5, 11.0]],
])
def test_solutions(kw, expected):
    assert Solution().averageOfLevels(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
