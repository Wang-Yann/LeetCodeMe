#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你字符串 s 和整数 k 。 
# 
#  请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。 
# 
#  英文中的 元音字母 为（a, e, i, o, u）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abciiidef", k = 3
# 输出：3
# 解释：子字符串 "iii" 包含 3 个元音字母。
#  
# 
#  示例 2： 
# 
#  输入：s = "aeiou", k = 2
# 输出：2
# 解释：任意长度为 2 的子字符串都包含 2 个元音字母。
#  
# 
#  示例 3： 
# 
#  输入：s = "leetcode", k = 3
# 输出：2
# 解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。
#  
# 
#  示例 4： 
# 
#  输入：s = "rhythms", k = 4
# 输出：0
# 解释：字符串 s 中不含任何元音字母。
#  
# 
#  示例 5： 
# 
#  输入：s = "tryhard", k = 4
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10^5 
#  s 由小写英文字母组成 
#  1 <= k <= s.length 
#  
#  Related Topics 字符串 Sliding Window

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l, ans = 0, 0
        window = 0
        lookup = set("aeiou")
        for r, char in enumerate(s):
            if char in lookup:
                window += 1
            while r - l + 1 > k:
                if s[l] in lookup:
                    window -= 1
                l += 1
            ans = max(ans, window)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(s="abciiidef", k=3), 3],
    [dict(s="aeiou", k=2), 2],
    [dict(s="leetcode", k=3), 2],
    [dict(s="rhythms", k=4), 0],
    [dict(s="tryhard", k=4), 1],
])
def test_solutions(kw, expected):
    assert Solution().maxVowels(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
