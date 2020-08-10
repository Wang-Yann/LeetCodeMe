#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 21:57:24
# @Last Modified : 2020-04-22 21:57:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 您需要在二叉树的每一行中找到最大的值。
#
#  示例：
#
#
# 输入:
#
#           1
#          / \
#         3   2
#        / \   \
#       5   3   9
#
# 输出: [1, 3, 9]
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 74 👎 0

from typing import List

import pytest

from common_utils import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        result = []
        level = 0
        queue = [root]
        while queue:
            length = len(queue)
            result.append(float("-inf"))
            for i in range(length):
                cur = queue.pop(0)
                result[level] = max(result[level], cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        1,
        left=TreeNode(2, right=TreeNode(4)),
        right=TreeNode(3, TreeNode(5, TreeNode(7), TreeNode(6)))
    )
    ), [1, 3, 5, 7]],
])
def test_solutions(kw, expected):
    assert Solution().largestValues(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
