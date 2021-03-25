#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对
# 了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。 
# 
#  请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。 
# 
#  请注意秘密数字和朋友的猜测数都可能含有重复数字。 
# 
#  示例 1: 
# 
#  输入: secret = "1807", guess = "7810"
# 
# 输出: "1A3B"
# 
# 解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。 
# 
#  示例 2: 
# 
#  输入: secret = "1123", guess = "0111"
# 
# 输出: "1A1B"
# 
# 解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。 
# 
#  说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。 
#  Related Topics 哈希表

"""
import collections
import operator

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getHint(self, secret: str, guess: str) -> str:
        A = sum(map(operator.eq, secret, guess))
        B = sum((collections.Counter(secret) & collections.Counter(guess)).values()) - A
        return "%dA%dB" % (A, B)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A, B = 0, 0
        s_lookup, g_lookup = collections.defaultdict(int), collections.defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                if s_lookup[g]:
                    s_lookup[g] -= 1
                    B += 1
                else:
                    g_lookup[g] += 1
                if g_lookup[s]:
                    g_lookup[s] -= 1
                    B += 1
                else:
                    s_lookup[s] += 1

        return "%dA%dB" % (A, B)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(secret="1807", guess="7810"), "1A3B"),
    pytest.param(dict(secret="1123", guess="0111"), "1A1B"),
    pytest.param(dict(secret="011", guess="110"), "1A2B"),
    pytest.param(dict(secret="1122", guess="1222"), "3A0B"),
])
def test_solutions(kwargs, expected):
    assert Solution().getHint(**kwargs) == expected
    assert Solution1().getHint(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
