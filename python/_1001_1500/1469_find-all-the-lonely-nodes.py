#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 16:59:19
# @Last Modified : 2020-08-07 16:59:19
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 二叉树中，如果一个节点是其父节点的唯一子节点，则称这样的节点为 “独生节点” 。二叉树的根节点不会是独生节点，因为它没有父节点。 
# 
#  给定一棵二叉树的根节点 root ，返回树中 所有的独生节点的值所构成的数组 。数组的顺序 不限 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,null,4]
# 输出：[4]
# 解释：浅蓝色的节点是唯一的独生节点。
# 节点 1 是根节点，不是独生的。
# 节点 2 和 3 有共同的父节点，所以它们都不是独生的。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2]
# 输出：[6,2]
# 输出：浅蓝色的节点是独生节点。
# 请谨记，顺序是不限的。 [2,6] 也是一种可接受的答案。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]
# 输出：[77,55,33,66,44,22]
# 解释：节点 99 和 88 有共同的父节点，节点 11 是根节点。
# 其他所有节点都是独生节点。 
# 
#  示例 4： 
# 
#  
# 输入：root = [197]
# 输出：[]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [31,null,78,null,28]
# 输出：[78,28]
#  
# 
#  
# 
#  提示： 
# 
#  
#  tree 中节点个数的取值范围是 [1, 1000]。 
#  每个节点的值的取值范围是 [1, 10^6]。 
#  
#  Related Topics 树 深度优先搜索 
#  👍 2 👎 0

"""

from typing import List

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
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(node, p):
            if not node:
                return
            if not (p.left and p.right):
                ans.append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)

        if not root:
            return []
        dfs(root.left, root)
        dfs(root.right, root)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def getLonelyNodes(self, root):
        def dfs(node):
            if not node:
                return
            if node.left and not node.right:
                result.append(node.left.val)
            elif node.right and not node.left:
                result.append(node.right.val)
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root)
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, left=TreeNode(2, right=TreeNode(4)), right=TreeNode(3))), [4]],
    [dict(root=TreeNode(7, left=TreeNode(1, left=TreeNode(6)),
                        right=TreeNode(4,
                                       left=TreeNode(5),
                                       right=TreeNode(3, right=TreeNode(2))
                                       ))), [2, 6]],

    [dict(root=TreeNode(11,
                        left=TreeNode(99, TreeNode(77, TreeNode(55, TreeNode(33)))),
                        right=TreeNode(88, None, TreeNode(66, None, TreeNode(44, None, TreeNode(22)))))
          ), [77, 55, 33, 66, 44, 22]],
    [dict(root=TreeNode(197)), []],
    [dict(root=TreeNode(31, right=TreeNode(78, right=TreeNode(28)))), [78, 28]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().getLonelyNodes(**kw)) == sorted(expected)
    assert sorted(Solution1().getLonelyNodes(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
