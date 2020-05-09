#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-09 22:23:46
# @Last Modified : 2020-05-09 22:23:46
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest

from common_utils import TreeNode


class Solution:

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        results = []

        def dfs(path, cur, sum_val):
            if not cur:
                return
            cur_val = cur.val
            if cur_val == sum_val and not cur.left and not cur.right:
                results.append(path + [cur_val])
                return
            path.append(cur_val)
            dfs(path, cur.left, sum_val - cur.val)
            dfs(path, cur.right, sum_val - cur.val)
            path.pop()

        dfs([], root, sum)
        return results


@pytest.mark.parametrize("root,sum,expected", [
    (
            TreeNode(5,
                     left=TreeNode(4, left=TreeNode(11, TreeNode(7), TreeNode(2))),
                     right=TreeNode(8, left=TreeNode(13), right=TreeNode(4, TreeNode(5), TreeNode(1)))
                     ),
            22,
            [
                [5, 4, 11, 2],
                [5, 8, 4, 5]
            ]

    ),
])
def test_solutions(root, sum, expected):
    assert Solution().pathSum(root, sum) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
