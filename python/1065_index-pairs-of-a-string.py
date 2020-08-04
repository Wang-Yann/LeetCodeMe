#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 14:20:34
# @Last Modified : 2020-08-04 14:20:34
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出 字符串 text 和 字符串列表 words, 返回所有的索引对 [i, j] 使得在索引对范围内的子字符串 text[i]...text[j]（包括
#  i 和 j）属于字符串列表 words。 
# 
#  
# 
#  示例 1: 
# 
#  输入: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# 输出: [[3,7],[9,13],[10,17]]
#  
# 
#  示例 2: 
# 
#  输入: text = "ababa", words = ["aba","ab"]
# 输出: [[0,1],[0,2],[2,3],[2,4]]
# 解释: 
# 注意，返回的配对可以有交叉，比如，"aba" 既在 [0,2] 中也在 [2,4] 中
#  
# 
#  
# 
#  提示: 
# 
#  
#  所有字符串都只包含小写字母。 
#  保证 words 中的字符串无重复。 
#  1 <= text.length <= 100 
#  1 <= words.length <= 20 
#  1 <= words[i].length <= 50 
#  按序返回索引对 [i,j]（即，按照索引对的第一个索引进行排序，当第一个索引对相同时按照第二个索引对排序）。 
#  
#  Related Topics 字典树 字符串 
#  👍 9 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        words = set(words)
        N = len(text)
        ans = []
        for i in range(N):
            txt = text[i:]
            for word in words:
                if txt.startswith(word):
                    ans.append([i, i + len(word) - 1])
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        text="thestoryofleetcodeandme", words=["story", "fleet", "leetcode"]
    ), [[3, 7], [9, 13], [10, 17]]],
    [dict(
        text="ababa", words=["aba", "ab"]
    ), [[0, 1], [0, 2], [2, 3], [2, 4]]],
])
def test_solutions(kw, expected):
    assert Solution().indexPairs(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
