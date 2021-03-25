#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 16:23:35
# @Last Modified : 2020-07-28 16:23:35
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k 个更新的操作。 
# 
#  其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endInd
# ex]（包括 startIndex 和 endIndex）增加 inc。 
# 
#  请你返回 k 次操作后的数组。 
# 
#  示例: 
# 
#  输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# 输出: [-2,0,3,5,3]
#  
# 
#  解释: 
# 
#  初始状态:
# [0,0,0,0,0]
# 
# 进行了操作 [1,3,2] 后的状态:
# [0,2,2,2,0]
# 
# 进行了操作 [2,4,3] 后的状态:
# [0,2,5,5,3]
# 
# 进行了操作 [0,2,-2] 后的状态:
# [-2,0,3,5,3]
#  
#  Related Topics 数组 
#  👍 26 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        """差分数组
        没用过真想不出
        """
        ans = [0] * length
        for s, e, v in updates:
            ans[s] += v
            if e + 1 < length:
                ans[e + 1] -= v
        for i in range(1, length):
            ans[i] += ans[i - 1]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]]), [-2, 0, 3, 5, 3]],
])
def test_solutions(kw, expected):
    assert Solution().getModifiedArray(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
