#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 16:00:45
# @Last Modified : 2020-07-28 16:00:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给你一棵二叉树，请按以下要求的顺序收集它的全部节点：
# 
#  
#  依次从左到右，每次收集并删除所有的叶子节点 
#  重复如上过程直到整棵树为空 
#  
# 
#  
# 
#  示例: 
# 
#  输入: [1,2,3,4,5]
#   
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# 
# 输出: [[4,5,3],[2],[1]]
#  
# 
#  
# 
#  解释: 
# 
#  1. 删除叶子节点 [4,5,3] ，得到如下树结构： 
# 
#            1
#          / 
#         2          
#  
# 
#  
# 
#  2. 现在删去叶子节点 [2] ，得到如下树结构： 
# 
#            1          
#  
# 
#  
# 
#  3. 现在删去叶子节点 [1] ，得到空树： 
# 
#            []         
#  
#  Related Topics 树 深度优先搜索 
#  👍 50 👎 0


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
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(node):
            """按照树高度分组"""
            if not node:
                return -1
            level = 1 + max(dfs(node.left), dfs(node.right))
            if len(res) - 1 < level:
                res.append([])
            res[level].append(node.val)
            return level

        dfs(root)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(1, left=TreeNode(2, TreeNode(4), TreeNode(5)), right=TreeNode(3))), [[4, 5, 3], [2], [1]]],
])
def test_solutions(kw, expected):
    assert Solution().findLeaves(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
