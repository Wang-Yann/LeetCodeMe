#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 14:04:04
# @Last Modified : 2020-08-05 14:04:04
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个「短语」列表 phrases，请你帮忙按规则生成拼接后的「新短语」列表。 
# 
#  「短语」（phrase）是仅由小写英文字母和空格组成的字符串。「短语」的开头和结尾都不会出现空格，「短语」中的空格不会连续出现。 
# 
#  「前后拼接」（Before and After puzzles）是合并两个「短语」形成「新短语」的方法。我们规定拼接时，第一个短语的最后一个单词 和 第二
# 个短语的第一个单词 必须相同。 
# 
#  返回每两个「短语」 phrases[i] 和 phrases[j]（i != j）进行「前后拼接」得到的「新短语」。 
# 
#  注意，两个「短语」拼接时的顺序也很重要，我们需要同时考虑这两个「短语」。另外，同一个「短语」可以多次参与拼接，但「新短语」不能再参与拼接。 
# 
#  请你按字典序排列并返回「新短语」列表，列表中的字符串应该是 不重复的 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：phrases = ["writing code","code rocks"]
# 输出：["writing code rocks"]
#  
# 
#  示例 2： 
# 
#  输入：phrases = ["mission statement",
#                 "a quick bite to eat",
#                "a chip off the old block",
#                "chocolate bar",
#                "mission impossible",
#                "a man on a mission",
#                "block party",
#                "eat my words",
#                "bar of soap"]
# 输出：["a chip off the old block party",
#      "a man on a mission impossible",
#      "a man on a mission statement",
#      "a quick bite to eat my words",
#       "chocolate bar of soap"]
#  
# 
#  示例 3： 
# 
#  输入：phrases = ["a","b","a"]
# 输出：["a"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= phrases.length <= 100 
#  1 <= phrases[i].length <= 100 
#  
#  Related Topics 字符串 
#  👍 7 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        """AC"""
        words = [x.split() for x in phrases]
        N = len(words)
        ans = set()
        for i in range(N):
            for j in range(N):
                if i != j and words[i][0] == words[j][-1]:
                    ans.add(" ".join(words[j] + words[i][1:]))
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(phrases=["writing code", "code rocks"]), ["writing code rocks"]],
    [dict(phrases=["a", "b", "a"]), ["a"]],
    [dict(phrases=["mission statement",
                   "a quick bite to eat",
                   "a chip off the old block",
                   "chocolate bar",
                   "mission impossible",
                   "a man on a mission",
                   "block party",
                   "eat my words",
                   "bar of soap"]),
     ["a chip off the old block party",
      "a man on a mission impossible",
      "a man on a mission statement",
      "a quick bite to eat my words",
      "chocolate bar of soap"]],
])
def test_solutions(kw, expected):
    assert Solution().beforeAndAfterPuzzles(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
