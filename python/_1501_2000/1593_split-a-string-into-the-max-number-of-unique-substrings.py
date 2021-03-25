#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-24 08:18:11
# @Last Modified : 2021-02-24 08:18:11
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 s ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。 
# 
#  字符串 s 拆分后可以得到若干 非空子字符串 ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 唯一的 。 
# 
#  注意：子字符串 是字符串中的一个连续字符序列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "ababccc"
# 输出：5
# 解释：一种最大拆分方法为 ['a', 'b', 'ab', 'c', 'cc'] 。像 ['a', 'b', 'a', 'b', 'c', 'cc'] 这样
# 拆分不满足题目要求，因为其中的 'a' 和 'b' 都出现了不止一次。
#  
# 
#  示例 2： 
# 
#  输入：s = "aba"
# 输出：2
# 解释：一种最大拆分方法为 ['a', 'ba'] 。
#  
# 
#  示例 3： 
# 
#  输入：s = "aa"
# 输出：1
# 解释：无法进一步拆分字符串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  
#  1 <= s.length <= 16 
#  
#  
#  s 仅包含小写英文字母 
#  
#  
#  Related Topics 回溯算法 
#  👍 21 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()

        def helper(cur_s):
            ans = 0
            if not cur_s:
                return 0
            for i in range(1, len(cur_s) + 1):
                candidate = cur_s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    ans = max(ans, 1 + helper(cur_s[i:]))
                    seen.remove(candidate)
            return ans

        return helper(s)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="ababccc"), 5],
    [dict(s="aba"), 2],
    [dict(s="aa"), 1],
])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    assert SolutionCLS().maxUniqueSplit(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
