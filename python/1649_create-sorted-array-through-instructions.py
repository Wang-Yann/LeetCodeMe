#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-22 10:17:09
# @Last Modified : 2021-02-22 10:17:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 instructions ，你需要根据 instructions 中的元素创建一个有序数组。一开始你有一个空的数组 nums ，你需要 从
# 左到右 遍历 instructions 中的元素，将它们依次插入 nums 数组中。每一次插入操作的 代价 是以下两者的 较小值 ： 
# 
#  
#  nums 中 严格小于 instructions[i] 的数字数目。 
#  nums 中 严格大于 instructions[i] 的数字数目。 
#  
# 
#  比方说，如果要将 3 插入到 nums = [1,2,3,5] ，那么插入操作的 代价 为 min(2, 1) (元素 1 和 2 小于 3 ，元素 5 
# 大于 3 ），插入后 nums 变成 [1,2,3,3,5] 。 
# 
#  请你返回将 instructions 中所有元素依次插入 nums 后的 总最小代价 。由于答案会很大，请将它对 109 + 7 取余 后返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：instructions = [1,5,6,2]
# 输出：1
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
# 插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
# 插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
# 总代价为 0 + 0 + 0 + 1 = 1 。 
# 
#  示例 2: 
# 
#  输入：instructions = [1,2,3,6,5,4]
# 输出：3
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
# 插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
# 插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
# 插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
# 插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。
#  
# 
#  示例 3： 
# 
#  输入：instructions = [1,3,3,3,2,4,2,1,2]
# 输出：4
# 解释：一开始 nums = [] 。
# 插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
# 插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
# 插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
# 插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
# ​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
# 插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
# 插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
# 总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= instructions.length <= 105 
#  1 <= instructions[i] <= 105 
#  
#  Related Topics 树状数组 线段树 二分查找 Ordered Map 
#  👍 22 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        Binary Indexed Tree 线段树
        https://leetcode.com/problems/create-sorted-array-through-instructions/discuss/927531/JavaC%2B%2BPython-Binary-Indexed-Tree
        """
        max_val = max(instructions)
        c = [0] * (max_val + 1)

        def update(x):
            while x <= max_val:
                c[x] += 1
                x += x & -x

        def get(x):
            ans = 0
            while x > 0:
                ans += c[x]
                x -= x & -x
            return ans

        res = 0
        for i, v in enumerate(instructions):
            res += min(get(v - 1), i - get(v))
            update(v)
        # print(c)
        return res % (10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(instructions=[1, 5, 6, 2]), 1],
    [dict(instructions=[1, 2, 3, 6, 5, 4]), 3],
    [dict(instructions=[1, 3, 3, 3, 2, 4, 2, 1, 2]), 4],
])
def test_solutions(kw, expected):
    assert Solution().createSortedArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
