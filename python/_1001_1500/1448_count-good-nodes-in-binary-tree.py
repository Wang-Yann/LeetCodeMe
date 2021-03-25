#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 23:58:48
# @Last Modified : 2020-07-09 23:58:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。 
# 
#  「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：root = [3,1,4,3,null,1,5]
# 输出：4
# 解释：图中蓝色节点为好节点。
# 根节点 (3) 永远是个好节点。
# 节点 4 -> (3,4) 是路径中的最大值。
# 节点 5 -> (3,4,5) 是路径中的最大值。
# 节点 3 -> (3,1,3) 是路径中的最大值。 
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [3,3,null,4,2]
# 输出：3
# 解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。 
# 
#  示例 3： 
# 
#  输入：root = [1]
# 输出：1
# 解释：根节点是好节点。 
# 
#  
# 
#  提示： 
# 
#  
#  二叉树中节点数目范围是 [1, 10^5] 。 
#  每个节点权值的范围是 [-10^4, 10^4] 。 
#  
#  Related Topics 树 深度优先搜索 
#  👍 5 👎 0


"""

import math

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        """
        AC
        """
        self.ans = 0

        def dfs(node, max_val):
            if not node:
                return
            if node.val >= max_val:
                # print(node.val)
                self.ans += 1
                max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, -math.inf)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(root=TreeNode(3, left=TreeNode(1, left=TreeNode(3)), right=TreeNode(4, TreeNode(1), TreeNode(5)))), 4],
    [dict(root=TreeNode(3, left=TreeNode(3, TreeNode(4), TreeNode(2)))), 3],
    [dict(root=TreeNode(1)), 1],

])
def test_solutions(kwargs, expected):
    assert Solution().goodNodes(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
