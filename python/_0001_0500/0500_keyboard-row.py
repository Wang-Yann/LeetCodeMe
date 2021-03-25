#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。 
# 
#  
# 
#  
# 
#  
# 
#  示例： 
# 
#  输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#  
# 
#  
# 
#  注意： 
# 
#  
#  你可以重复使用键盘上同一字符。 
#  你可以假设输入的字符串将只包含字母。 
#  Related Topics 哈希表

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hash_map = {**dict.fromkeys("qwertyuiop",1),
                    **dict.fromkeys("asdfghjkl",2),
                    **dict.fromkeys("zxcvbnm",3),
                    }
        ans = []
        for word in words:
            if len(set(hash_map.get(char.lower()) for char in word))==1:
                ans.append(word)
        return ans

# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
    (["asdfghjkl","qwertyuiop","zxcvbnm"], ["asdfghjkl","qwertyuiop","zxcvbnm"]),
])
def test_solutions(args, expected):
    assert Solution().findWords(args) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])

