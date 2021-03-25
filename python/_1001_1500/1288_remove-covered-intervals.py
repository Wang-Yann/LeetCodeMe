#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。 
# 
#  只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。 
# 
#  在完成所有删除操作后，请你返回列表中剩余区间的数目。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：intervals = [[1,4],[3,6],[2,8]]
# 输出：2
# 解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 1000 
#  0 <= intervals[i][0] < intervals[i][1] <= 10^5 
#  对于所有的 i != j：intervals[i] != intervals[j] 
#  
#  Related Topics Line Sweep

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        扫描线法
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = 0
        max_right = 0
        for l, r in intervals:
            if r > max_right:
                res += 1
            max_right = max(max_right, r)
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(intervals=[[1, 4], [3, 6], [2, 8]]), 2],
])
def test_solutions(kw, expected):
    assert Solution().removeCoveredIntervals(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
