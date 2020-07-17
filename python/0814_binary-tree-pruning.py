#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 16:41:32
# @Last Modified : 2020-04-24 16:41:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
# 给定二叉树根结点 root ，此外树的每个结点的值要么是 0，要么是 1。
#
#  返回移除了所有不包含 1 的子树的原二叉树。
#
#  ( 节点 X 的子树为 X 本身，以及所有 X 的后代。)
#
#
# 示例1:
# 输入: [1,null,0,0,1]
# 输出: [1,null,0,null,1]
#
# 解释:
# 只有红色节点满足条件“所有不包含 1 的子树”。
# 右图为返回的答案。
#
#
#
#
#
# 示例2:
# 输入: [1,0,1,0,0,0,1]
# 输出: [1,null,1,null,1]
#
#
#
#
#
#
# 示例3:
# 输入: [1,1,0,1,1,0,1,0]
# 输出: [1,1,0,1,1,null,1]
#
#
#
#
#
#  说明:
#
#
#  给定的二叉树最多有 100 个节点。
#  每个节点的值只会为 0 或 1 。
#
#  Related Topics 树
#  👍 96 👎 0

"""

from common_utils import TreeNode


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        """TODO
        注意
        if not root.left and not root.right and root.val == 0:
            return None
        判断放在上面得出不了正确结果,思考下为什么 ：
        需要后序遍历
        """
        if not root:
            return None
        # if not root.left and not root.right and root.val == 0:
        #     return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(0, TreeNode(0), TreeNode(1))),
        TreeNode(0, right=TreeNode(1, TreeNode(0), TreeNode(1))),

    ]
    lists = [x for x in samples]
    res = [sol.pruneTree(x) for x in lists]
    print(res)
