#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 22:57:00
# @Last Modified : 2020-05-06 22:57:00
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#  1
#  / \
#  2 2
#  / \ / \
# 3 4 4 3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#  1
#  / \
#  2 2
#  \ \
#  3 3
#
#
#
#  示例 1：
#
#  输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
#  示例 2：
#
#  输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 1000
#
#  注意：本题与主站 101 题相同：https://leetcode-cn.com/problems/symmetric-tree/
#  Related Topics 树
#  👍 54 👎 0


from common_utils import TreeNode


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if left and right:
                return left.val == right.val and helper(left.left, right.right) \
                       and helper(right.left, left.right)
            return False

        if not root:
            return True
        return helper(root.left, root.right)
