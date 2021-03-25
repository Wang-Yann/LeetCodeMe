#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 13:49:19
# @Last Modified : 2020-07-22 13:49:19
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。 
# 
#  你可以假定该序列中的数都是不相同的。 
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [5,2,6,1,3]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [5,2,1,3,6]
# 输出: true 
# 
#  进阶挑战： 
# 
#  您能否使用恒定的空间复杂度来完成此题？ 
#  Related Topics 栈 树 
#  👍 43 👎 0

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        """
        如果出现递减序列，则是左子树，否则是右子树；
        右子树一定是递增的
        待push进栈的节点值必须大于已经pop出来的所有元素的值，才能是合法的BST
        """
        low = -math.inf
        path = []
        for p in preorder:
            if p < low:
                return False
            while path and p > path[-1]:
                low = path.pop()
            path.append(p)
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([5, 2, 6, 1, 3], False),
    ([5, 2, 1, 3, 6], True),
])
def test_solutions255(args, expected):
    assert Solution().verifyPreorder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
