#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-25 06:11:55
# @Last Modified : 2021-02-25 06:11:55
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0


# 如果字符串 s 中 不存在 两个不同字符 频次 相同的情况，就称 s 是 优质字符串 。 
# 
#  给你一个字符串 s，返回使 s 成为 优质字符串 需要删除的 最小 字符数。 
# 
#  字符串中字符的 频次 是该字符在字符串中的出现次数。例如，在字符串 "aab" 中，'a' 的频次是 2，而 'b' 的频次是 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：0
# 解释：s 已经是优质字符串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "aaabbbcc"
# 输出：2
# 解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
# 另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。 
# 
#  示例 3： 
# 
#  
# 输入：s = "ceabaacb"
# 输出：2
# 解释：可以删除两个 'c' 得到优质字符串 "eabaab" 。
# 注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 105 
#  s 仅含小写英文字母 
#  
#  Related Topics 贪心算法 排序 
#  👍 17 👎 0


import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDeletions(self, s: str) -> int:
        """GOOD"""
        counter = collections.Counter(s)
        ans = 0
        used = set()
        for char, cnt in counter.items():
            while cnt > 0 and cnt in used:
                cnt -= 1
                ans += 1
            used.add(cnt)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="aab"), 0],
    [dict(s="aaabbbcc"), 2],
    [dict(s="ceabaacb"), 2],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().minDeletions(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
