#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 20:44:01
# @Last Modified : 2020-07-29 20:44:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个有 n 个整数的数组，你需要找到满足以下条件的三元组 (i, j, k) ： 
# 
#  
#  0 < i, i + 1 < j, j + 1 < k < n - 1 
#  子数组 (0, i - 1)，(i + 1, j - 1)，(j + 1, k - 1)，(k + 1, n - 1) 的和应该相等。 
#  
# 
#  这里我们定义子数组 (L, R) 表示原数组从索引为L的元素开始至索引为R的元素。 
# 
#  
# 
#  示例: 
# 
#  输入: [1,2,1,2,1,2,1]
# 输出: True
# 解释:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1
#  
# 
#  
# 
#  注意: 
# 
#  
#  1 <= n <= 2000。 
#  给定数组中的元素会在 [-1,000,000, 1,000,000] 范围内。 
#  
#  Related Topics 数组 
#  👍 16 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        """
        TODO TODO
        首先枚举中间点 j, 把区间先分成两段.
            初始化一个空集合
            取左边的那段区间, 枚举点 i, 如果点i分隔出来的两段的和相同, 则把这个和放入一个集合中
            取右边的那段区间, 枚举点 k, 如果点k分隔出来的两段的和相同并且这个值也在集合中出现了, 直接返回 true
            如果枚举完点 j 也没能返回 true, 说明没有这样的三元组, 返回 false即可.
        """
        N = len(nums)
        sum_array = [0] * N
        sum_array[0] = nums[0]
        for i in range(1, N):
            sum_array[i] = sum_array[i - 1] + nums[i]
        # print(sum_array)
        for j in range(3, N - 3):
            S = set()
            for i in range(1, j - 1):
                if sum_array[i - 1] == sum_array[j - 1] - sum_array[i]:
                    S.add(sum_array[i - 1])
            for k in range(j + 2, N - 1):
                x, y = sum_array[k - 1] - sum_array[j], sum_array[N - 1] - sum_array[k]
                if x == y and x in S:
                    return True
        return False


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 1, 2, 1, 2, 1]), True],
])
def test_solutions(kw, expected):
    assert Solution().splitArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
