#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  案例: 
# 
#  
# s = "leetcode"
# 返回 0.
# 
# s = "loveleetcode",
# 返回 2.
#  
# 
#  
# 
#  注意事项：您可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串

"""
import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for idx, val in enumerate(s):
            if counter[val] == 1:
                return idx
        return -1


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ("leetcode", 0),
    pytest.param("loveleetcode", 2),
])
def test_solutions(args, expected):
    assert Solution().firstUniqChar(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
