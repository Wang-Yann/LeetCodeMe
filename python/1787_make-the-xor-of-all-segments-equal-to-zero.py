#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-10 09:07:19
# @Last Modified : 2021-03-10 09:07:19
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 给你一个整数数组 nums 和一个整数 k 。区间 [left, right]（left <= right）的 异或结果 是对下标位于 left 和 rig
# ht（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR n
# ums[right] 。
#
#  返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,0,3,0], k = 1
# 输出：3
# 解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]
#
#
#  示例 2：
#
#
# 输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
# 输出：3
# 解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]
#
#
#  示例 3：
#
#
# 输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
# 输出：3
# 解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
#
#
#
#  提示：
#
#
#  1 <= k <= nums.length <= 2000
#  0 <= nums[i] < 210
#
#  Related Topics 动态规划
#  👍 14 👎 0
import collections
import time
from typing import List

import numpy
import pytest

# leetcode submit region begin(Prohibit modification and deletion)
from common_utils import memory_limit


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        """
        TODO
       https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/discuss/1097266/PythonC%2B%2B-DP-O(n)
        """
        N = len(nums)
        counters = [collections.Counter(nums[j] for j in range(i, N, k)) for i in range(k)]

        # case 1: one number is not from list
        mxs = [counters[i].most_common(1)[0][1] for i in range(k)]
        ans = N - (sum(mxs) - min(mxs))

        # case 2: all k numbers are from list
        d = counters[0]
        for i in range(1, k):
            d2 = collections.Counter()
            for x in d:
                for y in counters[i]:
                    t = x ^ y
                    d2[t] = max(d2[t], d[x] + counters[i][y])
            d = d2

        return min(ans, N - d[0])


# leetcode submit region end(Prohibit modification and deletion)


###限制内存和超时
@memory_limit(int(16e8))
@pytest.mark.xfail
def test_allocate():
    a = [numpy.arange(10 ** 8, dtype='u8') for i in range(10)]
    x = numpy.arange(3 * 10 ** 8, dtype='u8')
    print("Should fail")


@pytest.mark.timeout(12)
@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 0, 3, 0], k=1), 3],
    [dict(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3), 3],
    [dict(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3), 3],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    time.sleep(1)
    assert SolutionCLS().minChanges(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
