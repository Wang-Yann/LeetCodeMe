#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 06:37:50
# @Last Modified : 2021-02-24 06:37:50
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

# 给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。
# 
#  返回使字符串任意相邻两个字母不相同的最小删除成本。 
# 
#  请注意，删除一个字符后，删除其他字符的成本不会改变。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abaac", cost = [1,2,3,4,5]
# 输出：3
# 解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abc", cost = [1,2,3]
# 输出：0
# 解释：无需删除任何字母，因为字符串中不存在相邻两个字母相同的情况。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "aabaa", cost = [1,2,3,4,1]
# 输出：2
# 解释：删除第一个和最后一个字母，得到字符串 ("aba") 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  s.length == cost.length 
#  1 <= s.length, cost.length <= 10^5 
#  1 <= cost[i] <= 10^4 
#  s 中只含有小写英文字母 
#  
#  Related Topics 贪心算法 
#  👍 24 👎 0


from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """AC"""
    def minCost(self, s: str, cost: List[int]) -> int:
        ans = 0
        i = 0
        N = len(s)
        while i < N:
            j = i
            while j < N - 1 and s[j + 1] == s[i]:
                j += 1
            if j != i:
                ans += sum(cost[i:j + 1]) - max(cost[i:j + 1])
                i = j
            i += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abaac", cost=[1, 2, 3, 4, 5]), 3],
    [dict(s="abc", cost=[1, 2, 3]), 0],
    [dict(s="aabaa", cost=[1, 2, 3, 4, 1]), 2],
])
@pytest.mark.parametrize("SolutionCls", [Solution, ])
def test_solutions(kw, expected, SolutionCls):
    assert SolutionCls().minCost(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
