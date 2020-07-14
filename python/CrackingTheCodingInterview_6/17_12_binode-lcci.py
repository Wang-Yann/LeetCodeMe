#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 21:39:42
# @Last Modified : 2020-07-14 21:39:42
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉
# 搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。 
# 
#  返回转换后的单向链表的头节点。 
# 
#  注意：本题相对原题稍作改动 
# 
#  
# 
#  示例： 
# 
#  输入： [4,2,5,1,3,null,6,0]
# 输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
#  
# 
#  提示： 
# 
#  
#  节点数量不会超过 100000。 
#  
#  Related Topics 树 二叉搜索树 递归 
#  👍 28 👎 0


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

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(-1)
        self.pre = dummy

        def inOrder(root):
            if root:
                inOrder(root.left)
                root.left = None
                self.pre.right = root
                self.pre = root
                inOrder(root.right)

        inOrder(root)
        return dummy.right


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        root=TreeNode(
            4,
            left=TreeNode(2, TreeNode(1, left=TreeNode(0)), TreeNode(3)),
            right=TreeNode(5, right=TreeNode(6))
        )
    ),
        TreeNode(
            0,
            right=TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6))))))
        )
    ],

])
def test_solutions(kwargs, expected):
    assert repr(Solution().convertBiNode(**kwargs)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
