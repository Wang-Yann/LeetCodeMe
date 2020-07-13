#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:20:45
# @Last Modified : 2020-07-13 18:20:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你
# 会得到一张含有有效单词的列表。映射如下图所示： 
# 
#  
# 
#  示例 1: 
# 
#  输入: num = "8733", words = ["tree", "used"]
# 输出: ["tree", "used"]
#  
# 
#  示例 2: 
# 
#  输入: num = "2", words = ["a", "b", "c", "d"]
# 输出: ["a", "b", "c"] 
# 
#  提示： 
# 
#  
#  num.length <= 1000 
#  words.length <= 500 
#  words[i].length == num.length 
#  num中不会出现 0, 1 这两个数字 
#  
#  Related Topics 数组 
#  👍 11 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        kb = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        ns = list(num)
        candidate = words
        for i, num in enumerate(ns):
            candidate = [w for w in candidate if w[i] in kb[num]]

        return candidate


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(num="8733", words=["tree", "used"]), ["tree", "used"]],
    [dict(num="2", words=["a", "b", "c", "d"]), ["a", "b", "c"]],
])
def test_solutions(kw, expected):
    assert Solution().getValidT9Words(
        **kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
