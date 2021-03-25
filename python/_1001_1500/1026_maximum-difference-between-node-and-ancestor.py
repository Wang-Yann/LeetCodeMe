#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定二叉树的根节点 root，找出存在于不同节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。 
# 
#  （如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先） 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：[8,3,10,1,6,null,14,null,null,4,7,13]
# 输出：7
# 解释： 
# 我们有大量的节点与其祖先的差值，其中一些如下：
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# 在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数在 2 到 5000 之间。 
#  每个节点的值介于 0 到 100000 之间。 
#  
#  Related Topics 树 深度优先搜索

"""

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = -0x80000000

        def dfs(node, min_val, max_val):
            if not node:
                return 0
            val = node.val
            min_val = min(val, min_val)
            max_val = max(val, max_val)
            self.ans = max(self.ans, abs(max_val - min_val))
            if node.left:
                dfs(node.left, min_val, max_val)
            if node.right:
                dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)

# [8,3,10,1,6,null,14,null,null,4,7,13]
@pytest.mark.parametrize("args,expected", [
    (
            TreeNode(
                8,
                left=TreeNode(3, left=TreeNode(1), right=TreeNode(6, TreeNode(4), TreeNode(7))),
                right=TreeNode(10, right=TreeNode(14, left=TreeNode(13)))
            )
            , 7
    )
])
def test_solutions(args, expected):
    assert Solution().maxAncestorDiff(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
