#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-23 15:00:18
# @Last Modified : 2020-04-23 15:00:18
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉树，计算整个树的坡度。
#
#  一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
#
#  整个树的坡度就是其所有节点的坡度之和。
#
#
#
#  示例：
#
#  输入：
#          1
#        /   \
#       2     3
# 输出：1
# 解释：
# 结点 2 的坡度: 0
# 结点 3 的坡度: 0
# 结点 1 的坡度: |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
#
#
#
#
#  提示：
#
#
#  任何子树的结点的和不会超过 32 位整数的范围。
#  坡度的值不会超过 32 位整数的范围。
#
#  Related Topics 树
#  👍 76 👎 0

from common_utils import TreeNode


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        """
        Todo
        """

        def postOrder(cur, tilt):
            if not cur: return 0, tilt
            left_val, tilt = postOrder(cur.left, tilt)
            right_val, tilt = postOrder(cur.right, tilt)
            tilt += abs(left_val - right_val)
            return left_val + right_val + cur.val, tilt

        res = postOrder(root, 0)
        # print("Res", res)
        return res[1]


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, left=TreeNode(2), right=TreeNode(3)),
        TreeNode(1, left=TreeNode(2, TreeNode(4)), right=TreeNode(3)),
        TreeNode(1),
        TreeNode(1, TreeNode(2, left=TreeNode(4)), TreeNode(3, left=TreeNode(5))),
        None
    ]
    lists = [x for x in samples]
    res = [sol.findTilt(x) for x in lists]
    print(res)
