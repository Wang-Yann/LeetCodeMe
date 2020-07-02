#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出二叉树的根节点 root，树上每个节点都有一个不同的值。 
# 
#  如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。 
# 
#  返回森林中的每棵树。你可以按任意顺序组织答案。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
# 输出：[[1,2,null,4],[6],[7]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中的节点数最大为 1000。 
#  每个节点都有一个介于 1 到 1000 之间的值，且各不相同。 
#  to_delete.length <= 1000 
#  to_delete 包含一些从 1 到 1000、各不相同的值。 
#  
#  Related Topics 树 深度优先搜索

"""

from typing import List

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete = set(to_delete)

        def dfs(node, is_root):
            if not node:
                return None
            node_deleted = node.val in to_delete
            if is_root and not node_deleted:
                ans.append(node)
            node.left = dfs(node.left, node_deleted)
            node.right = dfs(node.right, node_deleted)
            return None if node_deleted else node

        dfs(root, True)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        1,
        left=TreeNode(2, TreeNode(4), TreeNode(5)),
        right=TreeNode(3, TreeNode(6), TreeNode(7)),
    ), to_delete=[3, 5]),
        [TreeNode(1, left=TreeNode(2, left=TreeNode(4))), TreeNode(6), TreeNode(7)]
    ],
])
def test_solutions(kw, expected):
    res = sorted(Solution().delNodes(**kw))
    for x, y in zip(res, sorted(expected)):
        assert repr(x) == repr(y)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
