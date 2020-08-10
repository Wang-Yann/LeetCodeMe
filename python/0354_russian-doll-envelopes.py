#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-29 22:15:23
# @Last Modified : 2020-04-29 22:15:23
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如
# 同俄罗斯套娃一样。
#
#  请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
#  说明:
# 不允许旋转信封。
#
#  示例:
#
#  输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#
#  Related Topics 二分查找 动态规划
#  👍 169 👎 0

"""

from typing import List

import pytest


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """在对信封按 w 进行排序以后，我们可以找到 h 上最长递增子序列的长度。"""
        LIS = []

        def insert(target):
            l, r = 0, len(LIS) - 1
            while l <= r:
                mid = (l + r) >> 1
                if LIS[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            if len(LIS) == l:
                LIS.append(target)
            else:
                LIS[l] = target
        # sort increasing in first dimension and decreasing on second
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        for envelope in envelopes:
            insert(envelope[1])
        # print(LIS )
        return len(LIS)


@pytest.mark.parametrize("args,expected", [
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    pytest.param([[1,2]], 1),
])
def test_solutions(args, expected):
    sol = Solution()
    assert sol.maxEnvelopes(args) == expected

if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
