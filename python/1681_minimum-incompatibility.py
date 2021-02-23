#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-23 03:53:07
# @Last Modified : 2021-02-23 03:53:07
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个整数数组 nums 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。 
# 
#  一个子集的 不兼容性 是该子集里面最大值和最小值的差。 
# 
#  请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。 
# 
#  子集的定义是数组中一些数字的集合，对数字顺序没有要求。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,1,4], k = 2
# 输出：4
# 解释：最优的分配是 [1,2] 和 [1,4] 。
# 不兼容性和为 (2-1) + (4-1) = 4 。
# 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [6,3,8,1,3,1,2,2], k = 4
# 输出：6
# 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
# 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,3,3,6,3,3], k = 3
# 输出：-1
# 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 16 
#  nums.length 能被 k 整除。 
#  1 <= nums[i] <= nums.length 
#  
#  Related Topics 贪心算法 回溯算法 
#  👍 32 👎 0

"""
import functools
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        """
        https://leetcode.com/problems/minimum-incompatibility/discuss/961392/Python-BruteforceDP
        """
        d = len(nums) // k  # the length of each partition

        @functools.lru_cache(None)
        def helper(arr):
            if not arr:
                return 0
            ret = 0x7fffffff
            for a in itertools.combinations(arr, d):  # choose a as a partition
                if len(set(a)) < d:  # check for duplicates
                    continue
                left = list(arr)  # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret = min(ret, max(a) - min(a) + helper(tuple(left)))
            return ret

        ans = helper(tuple(nums))  # turn the input into a tuple so the function can be cached
        return ans if ans != 0x7fffffff else -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 2, 1, 4], k=2), 4],
    [dict(nums=[6, 3, 8, 1, 3, 1, 2, 2], k=4), 6],
    [dict(nums=[5, 3, 3, 6, 3, 3], k=3), -1],
])
def test_solutions(kw, expected):
    assert Solution().minimumIncompatibility(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
