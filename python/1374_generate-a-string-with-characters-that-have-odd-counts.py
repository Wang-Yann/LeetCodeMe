#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-07 23:05:42
# @Last Modified : 2020-07-07 23:05:42
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个整数 n，请你返回一个含 n 个字符的字符串，其中每种字符在该字符串中都恰好出现 奇数次 。 
# 
#  返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出："pppz"
# 解释："pppz" 是一个满足题目要求的字符串，因为 'p' 出现 3 次，且 'z' 出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ohh
# h" 和 "love"。
#  
# 
#  示例 2： 
# 
#  输入：n = 2
# 输出："xy"
# 解释："xy" 是一个满足题目要求的字符串，因为 'x' 和 'y' 各出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ag" 和 "ur"。
# 
#  
# 
#  示例 3： 
# 
#  输入：n = 7
# 输出："holasss"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 500 
#  
#  Related Topics 字符串 
#  👍 6 👎 0


"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def generateTheString(self, n: int) -> str:
        """啥题目"""
        if n % 2:
            return "a" * n
        else:
            return "a" * (n - 1) + "b"


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=4), "pppz"),
    (dict(n=2), "xy"),
    (dict(n=7), "holasss"),
])
def test_solutions(kwargs, expected):
    res = Solution().generateTheString(**kwargs)
    counter = collections.Counter(res)
    assert all(cnt % 2 for k, cnt in counter.items())


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
