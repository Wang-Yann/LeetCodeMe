#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，使得 [1, n] 区间内的任何数字都
# 可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。 
# 
#  示例 1: 
# 
#  输入: nums = [1,3], n = 6
# 输出: 1 
# 解释:
# 根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
# 现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
# 其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
# 所以我们最少需要添加一个数字。 
# 
#  示例 2: 
# 
#  输入: nums = [1,5,10], n = 20
# 输出: 2
# 解释: 我们需要添加 [2, 4]。
#  
# 
#  示例 3: 
# 
#  输入: nums = [1,2,2], n = 5
# 输出: 0
#  
#  Related Topics 贪心算法

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    下面是这个贪心算法的流程：
    初始化区间 [1, miss) = [1, 1) = 空
    每当 n 没有被覆盖
    若当前元素 nums[i] 小于等于 miss
    将范围扩展到 [1, miss + nums[i])
    将 i 增加 1
    否则
    将 miss 添加到数组，将范围扩展到 [1, miss + miss)
    增加数字的计数
    返回增加数字的数目

    """

    def minPatches(self, nums: List[int], n: int) -> int:
        patch, i = 0, 0
        miss = 1
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patch += 1
        return patch


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[1, 5, 10], n=20), 2),
    pytest.param(dict(nums=[1, 3], n=6), 1),
    pytest.param(dict(nums=[1, 2, 2], n=5), 0),
])
def test_solutions(kwargs, expected):
    assert Solution().minPatches(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
