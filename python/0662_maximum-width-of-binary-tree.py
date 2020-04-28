#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-24 11:47:35
# @Last Modified : 2020-04-24 11:47:35
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution0:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        TODO
        """
        leftmosts = {}

        def dfs(node, pos, depth):
            """深度优先搜索"""
            if not node: return 0
            if depth >= len(leftmosts):
                # 对于每一个深度,第一个到达的位置会被记录
                leftmosts[depth] = pos
            return max(
                pos - leftmosts[depth] + 1,
                dfs(node.left, pos * 2, depth + 1),
                dfs(node.right, pos * 2 + 1, depth + 1),
            )

        res = dfs(root, 1, 0)
        return res


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        leftmosts = {}
        self.ans = 0

        def dfs(node, pos=0, depth=0):
            """深度优先搜索"""
            if node:
                # 对于每一个深度,第一个到达的位置会被记录 ,
                # 重点,pos只会写一次.　等价
                # leftmosts.setdefault(depth, pos)
                if depth not in leftmosts:
                    leftmosts[depth] = pos
                self.ans = max(self.ans, pos - leftmosts[depth] + 1)
                dfs(node.left, pos * 2, depth + 1)
                dfs(node.right, pos * 2 + 1, depth + 1)

        dfs(root)
        return self.ans


if __name__ == '__main__':
    sol = Solution()
    samples = [
        TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, right=TreeNode(9))),
        TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)))

    ]
    lists = [x for x in samples]
    res = [sol.widthOfBinaryTree(x) for x in lists]
    print(res)
