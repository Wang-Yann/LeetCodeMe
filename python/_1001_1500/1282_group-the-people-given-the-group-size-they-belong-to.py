#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 n 位用户参加活动，他们的 ID 从 0 到 n - 1，每位用户都 恰好 属于某一用户组。给你一个长度为 n 的数组 groupSizes，其中包含每
# 位用户所处的用户组的大小，请你返回用户分组情况（存在的用户组以及每个组中用户的 ID）。 
# 
#  你可以任何顺序返回解决方案，ID 的顺序也不受限制。此外，题目给出的数据保证至少存在一种解决方案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：groupSizes = [3,3,3,3,3,1,3]
# 输出：[[5],[0,1,2],[3,4,6]]
# 解释： 
# 其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。
#  
# 
#  示例 2： 
# 
#  输入：groupSizes = [2,1,3,3,3,2]
# 输出：[[1],[0,5],[2,3,4]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  groupSizes.length == n 
#  1 <= n <= 500 
#  1 <= groupSizes[i] <= n 
#  
#  Related Topics 贪心算法

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups, result = collections.defaultdict(list), []
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups.pop(size))
        return result


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = collections.defaultdict(list)
        for i, size in enumerate(groupSizes):
            groups[size].append(i)
        ans = []
        for size, ids in groups.items():
            if len(ids) == size:
                ans.append(ids)
            else:
                for i in range(len(ids) // size):
                    ans.append(ids[i:i + size])
        return ans


@pytest.mark.parametrize("kw,expected", [
    [dict(groupSizes=[3, 3, 3, 3, 3, 1, 3]), [[5], [0, 1, 2], [3, 4, 6]]],
    [dict(groupSizes=[2, 1, 3, 3, 3, 2]), [[1], [0, 5], [2, 3, 4]]],
])
def test_solutions(kw, expected):
    res = Solution().groupThePeople(**kw)
    for grp in res:
        size = len(grp)
        for u in grp:
            assert kw["groupSizes"][u] == size


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
