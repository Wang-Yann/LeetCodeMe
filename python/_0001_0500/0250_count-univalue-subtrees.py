#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 23:33:21
# @Last Modified : 2020-07-21 23:33:21
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

# 给定一个二叉树，统计该二叉树数值相同的子树个数。
# 
#  同值子树是指该子树的所有节点都拥有相同的数值。 
# 
#  示例： 
# 
#  输入: root = [5,1,5,5,5,null,5]
# 
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# 
# 输出: 4
#  
#  Related Topics 树 
#  👍 25 👎 0


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

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        """
        给定树中的一个结点，若其满足下面条件中的一个，则子树同值:
            该节点没有子结点 （基本情况）
            该节点的所有子结点都为同值子树，且结点与其子结点值相同。
        """

        def is_valid_part(node, val):
            """
            我们不检查结点是否有子结点，而是将 null 值看做同值子树，只是不计数
            """
            if node is None:
                return True

            # check if node.left and node.right are univalue subtrees of value node.val
            if not all([is_valid_part(node.left, node.val), is_valid_part(node.right, node.val)]):
                return False

            # if it passed the last step then this a valid subtree - increment
            self.count += 1

            # at this point we know that this node is a univalue subtree of value node.val
            # pass a boolean indicating if this is a valid subtree for the parent node
            return node.val == val

        self.count = 0
        is_valid_part(root, 0)
        return self.count


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        root=TreeNode(
            5,
            left=TreeNode(1, TreeNode(5), TreeNode(5)),
            right=TreeNode(5, right=TreeNode(5))
        )

    ), 4],

])
def test_solutions(kwargs, expected):
    assert Solution().countUnivalSubtrees(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
