#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。 
# 
#  给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s： 
# 
#  
#  s 是一个尽可能长的快乐字符串。 
#  s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。 
#  s 中只含有 'a'、'b' 、'c' 三种字母。 
#  
# 
#  如果不存在这样的字符串 s ，请返回一个空字符串 ""。 
# 
#  
# 
#  示例 1： 
# 
#  输入：a = 1, b = 1, c = 7
# 输出："ccaccbcc"
# 解释："ccbccacc" 也是一种正确答案。
#  
# 
#  示例 2： 
# 
#  输入：a = 2, b = 2, c = 1
# 输出："aabbc"
#  
# 
#  示例 3： 
# 
#  输入：a = 7, b = 1, c = 0
# 输出："aabaa"
# 解释：这是该测试用例的唯一正确答案。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= a, b, c <= 100 
#  a + b + c > 0 
#  
#  Related Topics 贪心算法 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        贪心
        """
        choices = [[a, "a"], [b, "b"], [c, "c"]]
        res = []
        for _ in range(a + b + c):
            choices.sort(reverse=True)
            for i, (cnt, char) in enumerate(choices):
                if cnt and res[-2:] != [char, char]:
                    res.append(char)
                    choices[i][0] -= 1
                    break
            # else:
            #     break
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(a=1, b=1, c=7), ["ccaccbcc", "ccbccacc"]),
    pytest.param(dict(a=2, b=2, c=1), ["aabbc", 'bacba']),
    pytest.param(dict(a=7, b=1, c=0), ["aabaa"]),
])
def test_solutions(kwargs, expected):
    assert Solution().longestDiverseString(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
