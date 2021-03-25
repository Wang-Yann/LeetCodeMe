#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。 
# 
#  回想一下： 
# 
#  
#  叶节点 是二叉树中没有子节点的节点 
#  树的根节点的 深度 为 0，如果某一节点的深度为 d，那它的子节点的深度就是 d+1 
#  如果我们假定 A 是一组节点 S 的 最近公共祖先，S 中的每个节点都在以 A 为根节点的子树中，且 A 的深度达到此条件下可能的最大值。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：root = [1,2,3]
# 输出：[1,2,3]
# 解释： 
# 最深的叶子是值为 2 和 3 的节点。
# 这些叶子的最近共同祖先是值为 1 的节点。
# 返回的答案为序列化的 TreeNode 对象（不是数组）"[1,2,3]" 。 
# 
#  示例 2： 
# 
#  输入：root = [1,2,3,4]
# 输出：[4]
#  
# 
#  示例 3： 
# 
#  输入：root = [1,2,3,4,5]
# 输出：[2,4,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  给你的树中将有 1 到 1000 个节点。 
#  树中每个节点的值都在 1 到 1000 之间。 
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

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """
        如果当前节点是最深叶子节点的最近公共祖先，那么它的左右子树的高度一定是相等的，否则高度低的那个子树的叶子节点深度一定比另一个子树的叶子节点的深度小
        """
        def dfs(node):
            if not node:
                return 0, None
            d1, lca1 = dfs(node.left)
            d2, lca2 = dfs(node.right)
            if d1 > d2:
                return d1 + 1, lca1
            elif d1 < d2:
                return d2 + 1, lca2
            else:
                return d1 + 1, node

        ans = dfs(root)[1]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))),
    (TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3)), TreeNode(4)),
])
def test_solutions(args, expected):
    assert repr(Solution().lcaDeepestLeaves(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
