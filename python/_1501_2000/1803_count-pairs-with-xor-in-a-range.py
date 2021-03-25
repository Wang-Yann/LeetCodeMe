#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-22 03:19:59
# @Last Modified : 2021-03-22 03:19:59
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
#
#  漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[
# j]) <= high 。
#
#
#
#  示例 1：
#
#  输入：nums = [1,4,2,7], low = 2, high = 6
# 输出：6
# 解释：所有漂亮数对 (i, j) 列出如下：
#     - (0, 1): nums[0] XOR nums[1] = 5
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
#
#
#  示例 2：
#
#  输入：nums = [9,8,4,2,1], low = 5, high = 14
# 输出：8
# 解释：所有漂亮数对 (i, j) 列出如下：
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 104
#  1 <= nums[i] <= 2 * 104
#  1 <= low <= high <= 2 * 104
#
#  Related Topics 字典树
#  👍 15 👎 0
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, val):
        node = self.root
        for i in reversed(range(15)):
            bit = (val >> i) & 1
            if bit not in node:
                node[bit] = {"cnt": 1}
            else:
                node[bit]["cnt"] += 1
            node = node[bit]

    def count(self, val, high):
        ans = 0
        node = self.root
        for i in reversed(range(15)):
            if not node:
                break
            bit = (val >> i) & 1
            cmp = (high >> i) & 1
            # if cmp == 1, then we know that all nodes having the same bit value as "val"
            # will result this digit to be 0 after xor,
            # which are guaranteed to be smaller than "high",
            #  so we can add all of those nodes and move onto the sub-trie
            # that have different value than "bit"
            # (1^bit is just a fancier way to say "change 0 to 1 and change 1 to 0")
            # otherwise, if cmp==0, we know all nodes
            #  that have different bit value as "val" will result something larger
            # so we can ignore all those and only traverse the sub-trie that has the same value as "bit"
            # (which, after xor, will result this digit to be zero)
            if cmp:
                if node.get(bit):
                    ans += node[bit]["cnt"]
                node = node.get(1 ^ bit, {})
            else:
                node = node.get(bit, {})
        return ans


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = Trie()

        ans = 0
        for x in nums:
            ans += trie.count(x, high + 1) - trie.count(x, low)
            trie.insert(x)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def countPairs(self, nums, low, high):
        def test(A, x):
            count = collections.Counter(A)
            res = 0
            while x:
                if x & 1:
                    res += sum(count[a] * count[(x - 1) ^ a] for a in count)
                count = collections.Counter({a >> 1: count[a] + count[a ^ 1] for a in count})
                x >>= 1
            return res // 2

        return test(nums, high + 1) - test(nums, low)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 4, 2, 7], low=2, high=6), 6],
    [dict(nums=[9, 8, 4, 2, 1], low=5, high=14), 8],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countPairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
