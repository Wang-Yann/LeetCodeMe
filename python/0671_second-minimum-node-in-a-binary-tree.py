#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 14:44:33
# @Last Modified : 2020-04-24 14:44:33
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一
# 个。
#
#  给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
#
#  示例 1:
#
#  输入:
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
#
#
#  示例 2:
#
#  输入:
#     2
#    / \
#   2   2
#
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
#
#  Related Topics 树
#  👍 87 👎 0


from common_utils import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        """中序遍历"""
        if not root: return None
        min_val, ans = root.val, float("inf")
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.val != min_val:
                ans = min(ans, cur.val)
            cur = cur.right
        return ans if ans != float("inf") else -1


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(2, TreeNode(2, TreeNode(5, TreeNode(5), TreeNode(7)))),
        TreeNode(2, TreeNode(2), TreeNode(2))

    ]
    lists = [x for x in samples]
    res = [sol.findSecondMinimumValue(x) for x in lists]
    print(res)
