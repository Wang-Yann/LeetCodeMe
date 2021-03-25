#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 11:48:08
# @Last Modified : 2020-08-07 11:48:08
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个 有序的 不相交区间列表 intervals 和一个要删除的区间 toBeRemoved， intervals 中的每一个区间 intervals[
# i] = [a, b] 都表示满足 a <= x < b 的所有实数 x 的集合。 
# 
#  我们将 intervals 中任意区间与 toBeRemoved 有交集的部分都删除。 
# 
#  返回删除所有交集区间后， intervals 剩余部分的 有序 列表。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# 输出：[[0,1],[6,7]]
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[0,5]], toBeRemoved = [2,3]
# 输出：[[0,2],[3,5]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 10^4 
#  -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9 
#  
#  Related Topics 数学 Line Sweep 
#  👍 9 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        toL, toR = toBeRemoved
        ans = list()
        for s, e in intervals:
            if toL >= e or toR <= s:
                ans.append([s, e])
            else:
                if toL > s:
                    ans.append([s, toL])
                if toR < e:
                    ans.append([toR, e])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(intervals=[[0, 2], [3, 4], [5, 7]], toBeRemoved=[1, 6]), [[0, 1], [6, 7]]],
    [dict(intervals=[[0, 5]], toBeRemoved=[2, 3]), [[0, 2], [3, 5]]],
])
def test_solutions(kw, expected):
    assert Solution().removeInterval(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
