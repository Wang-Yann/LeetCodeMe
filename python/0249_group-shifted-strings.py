#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 23:18:17
# @Last Modified : 2020-07-21 23:18:17
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，比如："abc" -> "bcd"。这样，我们可
# 以持续进行 “移位” 操作，从而生成如下移位序列： 
# 
#  "abc" -> "bcd" -> ... -> "xyz" 
# 
#  给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。 
# 
#  
# 
#  示例： 
# 
#  输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
# 输出：
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# 解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。 
#  Related Topics 哈希表 字符串 
#  👍 20 👎 0

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """AC"""

        def get_key(x):
            return tuple((ord(x[i]) - ord(x[0]) + 26) % 26 for i in range(len(x)))

        ans = collections.defaultdict(list)
        for s in strings:
            ans[get_key(s)].append(s)

        return list(ans.values())


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
            ,
            [
                ["abc", "bcd", "xyz"],
                ["az", "ba"],
                ["acef"],
                ["a", "z"]
            ]
    ),
])
def test_solutions(args, expected):
    assert sorted(Solution().groupStrings(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
