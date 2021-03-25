#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 16:49:09
# @Last Modified : 2020-07-21 16:49:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。 
# 
#  示例： 
# 
#  输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
# 输出: ["2", "4->49", "51->74", "76->99"]
#  
#  Related Topics 数组 
#  👍 20 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """AC"""
        ans = []
        nums = [lower - 1] + nums + [upper + 1]
        N = len(nums)
        for i in range(N - 1):
            cur_start = nums[i] + 1
            if nums[i + 1] - cur_start == 1:
                ans.append(str(cur_start))
            elif nums[i + 1] - cur_start > 1:
                ans.append("{}->{}".format(cur_start, nums[i + 1] - 1))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[0, 1, 3, 50, 75], lower=0, upper=99, ),
     ["2", "4->49", "51->74", "76->99"]],
])
def test_solutions(kw, expected):
    assert Solution().findMissingRanges(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
