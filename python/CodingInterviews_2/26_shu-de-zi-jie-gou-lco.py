#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 23:53:21
# @Last Modified : 2020-05-05 23:53:21
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
#  例如:
# 给定的树 A:
#
#  3
#  / \
#  4 5
#  / \
#  1 2
# 给定的树 B：
#
#  4
#  /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
#
#  示例 1：
#
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#
#
#  示例 2：
#
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true
#
#  限制：
#
#  0 <= 节点个数 <= 10000
#  Related Topics 树
#  👍 79 👎 0




import pytest

from common_utils import TreeNode


class Solution:

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def helper(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False
            return helper(A.left, B.left) and helper(A.right, B.right)

        return bool(A and B) and (
                helper(A, B)
                or self.isSubStructure(A.left, B)
                or self.isSubStructure(A.right, B)
        )


@pytest.mark.parametrize("args,expected", [
    [(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, right=TreeNode(3))), True],
])
def test_solutions(args, expected):
    assert Solution().isSubStructure(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
