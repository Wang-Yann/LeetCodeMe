#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 21:01:19
# @Last Modified : 2020-07-16 21:01:19
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请
# 求出最少可以切成多少个子数组。 
# 
#  示例 1： 
# 
#  
#  输入：nums = [2,3,3,2,3,3] 
# 
#  输出：2 
# 
#  解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。 
#  
# 
#  示例 2： 
# 
#  
#  输入：nums = [2,3,5,7] 
# 
#  输出：4 
# 
#  解释：只有一种可行的切割：[2], [3], [5], [7] 
#  
# 
#  限制： 
# 
#  
#  1 <= nums.length <= 10^5 
#  2 <= nums[i] <= 10^6 
#  
#  👍 17 👎 0


"""

import pytest

# leetcode submit region begin(Prohibit modification and deletion)
#
max_num = INF = 10 ** 6
min_factor = [1] * (max_num + 1)
p = 2

# O(M loglog M)
while p <= max_num:
    i = p
    while i * p <= max_num:
        if min_factor[i * p] == 1:
            min_factor[i * p] = p
        i += 1

    p += 1
    while p <= max_num:
        if min_factor[p] == 1:
            break
        p += 1
# print(min_factor[:122])

class Solution:
    """ XX这题目还要素数打表"""

    def splitArray(self, nums) -> int:

        f = {}
        n = len(nums)

        x = nums[0]
        while True:
            if min_factor[x] == 1:
                f[x] = 1
                break

            f[min_factor[x]] = 1
            x //= min_factor[x]

        min_prev = 1
        for i in range(1, n):
            x = nums[i]

            min_cur = INF
            while True:
                if min_factor[x] == 1:
                    f[x] = min(f.get(x, INF), min_prev + 1)
                    min_cur = min(min_cur, f[x])
                    break

                f[min_factor[x]] = min(f.get(min_factor[x], INF), min_prev + 1)
                min_cur = min(min_cur, f[min_factor[x]])
                x //= min_factor[x]

            min_prev = min_cur

        return min_prev


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[2, 3, 3, 2, 3, 3]), 2],

    pytest.param(dict(nums=[2, 3, 5, 7]), 4),
])
def test_solutions(kwargs, expected):
    assert Solution().splitArray(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
