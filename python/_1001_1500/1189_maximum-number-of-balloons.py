#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。 
# 
#  字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：text = "nlaebolko"
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：text = "loonbalxballpoon"
# 输出：2
#  
# 
#  示例 3： 
# 
#  输入：text = "leetcode"
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= text.length <= 10^4 
#  text 全部由小写英文字母组成 
#  
#  Related Topics 哈希表 字符串

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = collections.Counter(text)
        balloon = collections.Counter("balloon")
        return min(counter[char] // balloon[char] for char in balloon)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(text="nlaebolko"), 1],
    [dict(text="loonbalxballpoon"), 2],
    [dict(text="leetcode"), 0],
])
def test_solutions(kw, expected):
    assert Solution().maxNumberOfBalloons(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
