#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 13:24:44
# @Last Modified : 2020-08-09 13:24:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你二叉树的根节点 root 和一个整数 distance 。 
# 
#  如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。 
# 
#  返回树中 好叶子节点对的数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 
#  输入：root = [1,2,3,null,4], distance = 3
# 输出：1
# 解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6,7], distance = 3
# 输出：2
# 解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。
#  
# 
#  示例 3： 
# 
#  输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# 输出：1
# 解释：唯一的好叶子节点对是 [2,5] 。
#  
# 
#  示例 4： 
# 
#  输入：root = [100], distance = 1
# 输出：0
#  
# 
#  示例 5： 
# 
#  输入：root = [1,1,1], distance = 2
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  tree 的节点数在 [1, 2^10] 范围内。 
#  每个节点的值都在 [1, 100] 之间。 
#  1 <= distance <= 10 
#  
#  Related Topics 树 深度优先搜索 
#  👍 25 👎 0
	 

"""
import collections

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node, dist):
            """
            # 对于 dfs(root,distance)，同时返回：
            # 每个叶子节点与 root 之间的距离
            # 以 root 为根节点的子树中好叶子节点对的数量

            """
            # 对于 dfs(root,distance)，同时返回：
            # 每个叶子节点与 root 之间的距离
            # 以 root 为根节点的子树中好叶子节点对的数量

            depths = [0] * (dist + 1)
            isLeaf = not node.left and not node.right
            if isLeaf:
                depths[0] = 1
                return depths, 0

            leftDepths, rightDepths = [0] * (dist + 1), [0] * (dist + 1)
            leftCount = rightCount = 0

            if node.left:
                leftDepths, leftCount = dfs(node.left, dist)
            if node.right:
                rightDepths, rightCount = dfs(node.right, dist)

            for i in range(dist):
                depths[i + 1] += leftDepths[i]
                depths[i + 1] += rightDepths[i]

            cnt = 0
            # 两个以 P 为最近公共祖先的叶子节点 A、B，其中一个（例如 A）在以  left 为根的子树中，另一个（例如 B）在以 right 为根的子树中
            # A 与 B 之间的距离，就等于 A 与  left 之间的距离，加上 B  与  right 之间的距离，再加上 2

            for i in range(dist + 1):
                for j in range((dist - 2) + 1 - i):
                    cnt += leftDepths[i] * rightDepths[j]
            # print(depths,leftDepths,rightDepths)

            return depths, cnt + leftCount + rightCount

        return dfs(root, distance)[1]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        self.res = 0

        def dfs(node, depth):
            if not node.left and not node.right:
                return collections.Counter([depth])
            l_counter, r_counter = collections.Counter(), collections.Counter()
            if node.left:
                l_counter = dfs(node.left, depth + 1)
            if node.right:
                r_counter = dfs(node.right, depth + 1)
            # print(l_counter,r_counter)
            for l_d in l_counter:
                self.res += l_counter[l_d] * sum(r_counter[r_d] for r_d in r_counter if r_d + l_d - 2 * depth <= distance)
            return l_counter + r_counter

        dfs(root, 0)
        return self.res


@pytest.mark.parametrize("kwargs,expected", [
    [dict(root=TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)), distance=3), 1],
    [dict(root=TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)),
                        right=TreeNode(3, TreeNode(6), TreeNode(7))), distance=3), 2],
    [dict(
        root=TreeNode(7,
                      left=TreeNode(1, TreeNode(6)),
                      right=TreeNode(4, TreeNode(5), TreeNode(3, right=TreeNode(2))))

        , distance=3), 1],
    [dict(root=TreeNode(100), distance=1), 0],
    [dict(root=TreeNode(1, TreeNode(1), TreeNode(1)), distance=2), 1],

])
def test_solutions(kwargs, expected):
    assert Solution().countPairs(**kwargs) == expected
    assert Solution1().countPairs(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
