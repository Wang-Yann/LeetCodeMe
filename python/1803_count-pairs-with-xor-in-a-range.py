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


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Trie:  # trie
    def __init__(self):
        self.tree = {}

    def insert(self, s):
        curr = self.tree
        for ch in s:
            if "#" not in curr:
                curr["#"] = 0  # calculate element number
            curr["#"] += 1
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        if "#" not in curr:
            curr["#"] = 0
        curr["#"] += 1

    def query(self, s1, limit, digit, curr):
        if digit < 0:  # end recursion
            return curr["#"]
        p = 1 << digit
        ch = s1[16 - digit]  # current char
        if ch == '1':
            och = '0'  # opposite char
        else:
            och = '1'
        res = 0
        if p > limit:
            if ch in curr:
                res += self.query(s1, limit, digit - 1, curr[ch])
        else:
            if och in curr:
                res += self.query(s1, limit - p, digit - 1, curr[och])
            if ch in curr:
                res += curr[ch]["#"]
        return res


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        """HARD"""
        res = 0
        trie = Trie()

        for num in nums:
            # calculate then insert
            s = bin(num)[2:]
            s = "0" * (17 - len(s)) + s
            hi = trie.query(s, high, 16, trie.tree)
            lo = trie.query(s, low - 1, 16, trie.tree)
            res += hi - lo
            trie.insert(s)

        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 4, 2, 7], low=2, high=6), 6],
    [dict(nums=[9, 8, 4, 2, 1], low=5, high=14), 8],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().countPairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
