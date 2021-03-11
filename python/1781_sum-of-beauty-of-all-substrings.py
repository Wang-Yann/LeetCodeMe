#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-03-11 02:26:06
# @Last Modified : 2021-03-11 02:26:06
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 一个字符串的 美丽值 定义为：出现频率最高字符与出现频率最低字符的出现次数之差。 
# 
#  
#  比方说，"abaacc" 的美丽值为 3 - 1 = 2 。 
#  
# 
#  给你一个字符串 s ，请你返回它所有子字符串的 美丽值 之和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aabcb"
# 输出：5
# 解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。 
# 
#  示例 2： 
# 
#  
# 输入：s = "aabcbaa"
# 输出：17
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
#  Related Topics 哈希表 字符串 
#  👍 5 👎 0


import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def beautySum(self, s: str) -> int:
        """暴力"""
        ans = 0
        N = len(s)
        for i in range(N):
            counter = collections.Counter()
            for j in range(i, N):
                counter[s[j]] += 1
                ans += max(counter.values()) - min(counter.values())
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aabcb"), 5],
    [dict(s="aabcbaa"), 17],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().beautySum(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
