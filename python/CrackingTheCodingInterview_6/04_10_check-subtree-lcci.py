#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:35:08
# @Last Modified : 2020-07-12 21:35:08
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。 
# 
#  如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。 
# 
#  示例1: 
# 
#   输入：t1 = [1, 2, 3], t2 = [2]
#  输出：true
#  
# 
#  示例2: 
# 
#   输入：t1 = [1, null, 2, 4], t2 = [3, 2]
#  输出：false
#  
# 
#  提示： 
# 
#  
#  树的节点数目范围为[0, 20000]。 
#  
#  Related Topics 树 
#  👍 14 👎 0


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

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None:
            return t2 is None
        if t2 is None:
            return True
        if t1.val == t2.val:
            return self.checkSubTree(t1.left, t2.left) and self.checkSubTree(t1.right, t2.right)
        return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(t1=TreeNode(1, TreeNode(2), TreeNode(3)), t2=TreeNode(2)), True],
    [dict(t1=TreeNode(1, right=TreeNode(2, left=TreeNode(4))), t2=TreeNode(3, left=TreeNode(2))), False],

])
def test_solutions(kwargs, expected):
    assert Solution().checkSubTree(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
