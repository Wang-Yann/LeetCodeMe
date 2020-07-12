#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:21:46
# @Last Modified : 2020-07-12 21:21:46
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。 
# 
#  如果指定节点没有对应的“下一个”节点，则返回null。 
# 
#  示例 1: 
# 
#  输入: root = [2,1,3], p = 1
# 
#   2
#  / \
# 1   3
# 
# 输出: 2 
# 
#  示例 2: 
# 
#  输入: root = [5,3,6,2,4,null,null,1], p = 6
# 
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /   
# 1
# 
# 输出: null 
#  Related Topics 树 深度优先搜索 
#  👍 22 👎 0


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

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        """
        如果 p 大于当前节点的值，说明后继节点一定在 RightTree
        如果 p 等于当前节点的值，说明后继节点一定在 RightTree
        如果 p 小于当前节点的值，说明后继节点一定在 LeftTree 或自己就是
        递归调用 LeftTree，如果是空的，说明当前节点就是答案
        如果不是空的，则说明在 LeftTree 已经找到合适的答案，直接返回即可

        """
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if not left:
                return root
            else:
                return left


# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    p = TreeNode(1)
    root = TreeNode(2, left=p, right=TreeNode(3))
    res = Solution().inorderSuccessor(root, p)
    assert repr(res) == repr(root)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
