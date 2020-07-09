#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn’
# t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一
# 本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。 
# 
# 
#  注意：本题相对原题稍作改动，只需返回未识别的字符数 
# 
#  
# 
#  示例： 
# 
#  输入：
# dictionary = ["looked","just","like","her","brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
#  
# 
#  提示： 
# 
#  
#  0 <= len(sentence) <= 1000 
#  dictionary中总字符数不超过 150000。 
#  你可以认为dictionary和sentence中只包含小写字母。 
#  
#  Related Topics 记忆化 字符串

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        lookup = set(dictionary)
        N = len(sentence)
        dp = [0] * (N + 1)
        for i in range(1, N + 1):
            dp[i] = dp[i - 1] + 1
            for word in lookup:
                lw = len(word)
                if sentence[max(i - lw, 0):i] == word:
                    dp[i] = min(dp[i], dp[i - lw])
        # print(dp)
        return dp[N]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        dictionary=["looked", "just", "like", "her", "brother"],
        sentence="jesslookedjustliketimherbrother"
    ), 7],
])
def test_solutions(kw, expected):
    assert Solution().respace(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
