#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 16:11:45
# @Last Modified : 2020-07-31 16:11:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个关键词集合 words 和一个字符串 S，将所有 S 中出现的关键词加粗。所有在标签 <b> 和 </b> 中的字母都会加粗。 
# 
#  返回的字符串需要使用尽可能少的标签，当然标签应形成有效的组合。 
# 
#  例如，给定 words = ["ab", "bc"] 和 S = "aabcd"，需要返回 "a<b>abc</b>d"。注意返回 "a<b>a<b>b<
# /b>c</b>d" 会使用更多的标签，因此是错误的。 
# 
#  
# 
#  注： 
# 
#  
#  words 长度的范围为 [0, 50]。 
#  words[i] 长度的范围为 [1, 10]。 
#  S 长度的范围为 [0, 500]。 
#  所有 words[i] 和 S 中的字符都为小写字母。 
#  
# 
#  
#  Related Topics 字符串 
#  👍 22 👎 0

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        """和616重复"""
        N = len(S)
        mask = [False] * N
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i + len(word), N)):
                        mask[j] = True
        # print(mask)
        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda x: x[1]):
            # print(incl,list(grp))
            if incl:
                ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl:
                ans.append("</b>")
        return "".join(ans)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(words=["ab", "bc"], S="aabcd"), "a<b>abc</b>d"],
])
def test_solutions(kw, expected):
    assert Solution().boldWords(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
