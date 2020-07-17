#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:49:42
# @Last Modified : 2020-04-22 10:49:42
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
#  说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
#  示例 1:
#
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1
#
#  示例 2:
#
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3
#
#  进阶：
# 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？
#  Related Topics 树 二分查找
#  👍 246 👎 0

from common_utils import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root or not k:return None
        cur = root
        stack = []
        idx=0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            idx+=1
            if idx==k:
                return cur.val
            cur=cur.right


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(3,
                 left=TreeNode(1, right=TreeNode(2)),
                 right=TreeNode(4)
                 ),
        TreeNode(5,
                 left=TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)),
                 right=TreeNode(6)
                 )

    ]
    lists = [x for x in samples]
    res = [sol.kthSmallest(x,3) for x in lists]
    print(res)
