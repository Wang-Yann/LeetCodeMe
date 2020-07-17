#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-22 22:09:57
# @Last Modified : 2020-04-22 22:09:57
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。
#
#
#
#  示例：
#
#  输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树节点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
#
#
#  注意：
#
#
#  二叉树的大小范围在 2 到 100。
#  二叉树总是有效的，每个节点的值都是整数，且不重复。
#  本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
#
#  Related Topics 树 递归
#  👍 65 👎 0


from common_utils import TreeNode


class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        prev = float('-inf')
        ans = float('inf')

        def inOrderTraversal(node):
            nonlocal prev, ans
            if node:
                inOrderTraversal(node.left)
                ans = min(ans, node.val - prev)
                prev = node.val
                inOrderTraversal(node.right)

        inOrderTraversal(root)
        return ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, right=TreeNode(3, TreeNode(2))),
        TreeNode(12),
        None
    ]
    res = [sol.minDiffInBST(x) for x in samples]
    print(res)
