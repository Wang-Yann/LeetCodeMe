#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:16:11
# @Last Modified : 2020-05-05 16:16:11
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个包含 非负数 的数组和一个目标 整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，且总和为 k 的倍数，即总和为 n*k，其
# 中 n 也是一个整数。
#
#
#
#  示例 1：
#
#  输入：[23,2,4,6,7], k = 6
# 输出：True
# 解释：[2,4] 是一个大小为 2 的子数组，并且和为 6。
#
#
#  示例 2：
#
#  输入：[23,2,6,4,7], k = 6
# 输出：True
# 解释：[23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
#
#
#
#
#  说明：
#
#
#  数组的长度不会超过 10,000 。
#  你可以认为所有数字总和在 32 位有符号整数范围内。
#
#  Related Topics 数学 动态规划
#  👍 130 👎 0

from typing import List

import pytest


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cnt = 0
        lookup = {0: -1}
        # 我们使用 HashMap 来保存到第 ii 个元素为止的累积和
        for i, num in enumerate(nums):
            cnt += num
            if k:
                cnt %= k
            if cnt in lookup:
                if i - lookup[cnt] >= 2:
                    return True
            else:
                lookup[cnt] = i
        return False


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[23, 2, 4, 6, 7], k=6), True),
    pytest.param(dict(nums=[23, 2, 6, 4, 7], k=6), True),
])
def test_solutions(kwargs, expected):
    assert Solution().checkSubarraySum(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
