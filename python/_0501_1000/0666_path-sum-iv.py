#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 10:56:46
# @Last Modified : 2020-07-31 10:56:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。 
# 
#  对于每个整数： 
# 
#  
#  百位上的数字表示这个节点的深度 D，1 <= D <= 4。 
#  十位上的数字表示这个节点在当前层所在的位置 P， 1 <= P <= 8。位置编号与一棵满二叉树的位置编号相同。 
#  个位上的数字表示这个节点的权值 V，0 <= V <= 9。 
#  
# 
#  给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，请你返回从根到所有叶子结点的路径之和。 
# 
#  样例 1: 
# 
#  输入: [113, 215, 221]
# 输出: 12
# 解释: 
# 这棵树形状如下:
#     3
#    / \
#   5   1
# 
# 路径和 = (3 + 5) + (3 + 1) = 12.
#  
# 
#  
# 
#  样例 2: 
# 
#  输入: [113, 221]
# 输出: 4
# 解释: 
# 这棵树形状如下: 
#     3
#      \
#       1
# 
# 路径和 = (3 + 1) = 4.
#  
# 
#  
#  Related Topics 树 
#  👍 16 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        values = {x // 10: x % 10 for x in nums}

        def dfs(node, running_sum=0):
            """
            一个省时的想法是，我们根据等式 root = num / 10 = 10 * depth + pos 作为根节点的唯一标识符。
            则左子结点的标识符是 left = 10 * (depth + 1) + 2 * pos - 1，而右子节点则是 right = left + 1。

            """
            if node not in values:
                return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] // 10)
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[113, 215, 221]), 12],
    [dict(nums=[113, 221]), 4],
])
def test_solutions(kw, expected):
    assert Solution().pathSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
