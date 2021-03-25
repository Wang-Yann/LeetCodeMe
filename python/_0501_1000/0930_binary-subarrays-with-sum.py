#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在由若干 0 和 1 组成的数组 A 中，有多少个和为 S 的非空子数组。 
# 
#  
# 
#  示例： 
# 
#  输入：A = [1,0,1,0,1], S = 2
# 输出：4
# 解释：
# 如下面黑体所示，有 4 个满足题目要求的子数组：
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  A.length <= 30000 
#  0 <= S <= A.length 
#  A[i] 为 0 或 1 
#  
#  Related Topics 哈希表 双指针

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        """
        这样就可以通过 P[j + 1] - P[i] = A[i] + A[i + 1] + ... + A[j] 快速计算出 A[i..j] 的和。
        我们可以对数组 P 进行一次线性扫描，当扫描到 P[j] 时，我们需要得到的是满足 P[j] = P[i] + S 且 i < j 的 i 的数目，
        使用计数器（map 或 dict）可以满足要求

        GOOD   TODO TODO
        """
        prefix = [0]
        for v in A:
            prefix.append(prefix[-1] + v)
        counter = collections.Counter()
        ans = 0
        # print(prefix)
        for x in prefix:
            # print(counter,x)
            ans += counter[x]
            counter[x + S] += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[1, 0, 1, 0, 1], S=2), 4],
])
def test_solutions(kw, expected):
    assert Solution().numSubarraysWithSum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
