#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-30 08:00:00
# @Last Modified : 2020-06-30 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 
# 个字符。） 
# 
#  给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。只有在待查项 queries[i] 与模式串 patt
# ern 匹配时， answer[i] 才为 true，否则为 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# , pattern = "FB"
# 输出：[true,false,true,true,false]
# 示例：
# "FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
# "FootBall" 可以这样生成："F" + "oot" + "B" + "all".
# "FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer". 
# 
#  示例 2： 
# 
#  输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# , pattern = "FoBa"
# 输出：[true,false,true,false,false]
# 解释：
# "FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
# "FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".
#  
# 
#  示例 3： 
# 
#  输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# , pattern = "FoBaT"
# 输入：[false,true,false,false,false]
# 解释： 
# "FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= queries.length <= 100 
#  1 <= queries[i].length <= 100 
#  1 <= pattern.length <= 100 
#  所有字符串都仅由大写和小写英文字母组成。 
#  
#  Related Topics 字典树 字符串

"""
import re
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        """垃圾题目　题意不清晰"""
        r = re.compile("^" + "[a-z]*".join([""]+list(pattern) + [""]) + "$")
        # print(r)
        return list(bool(r.match(word)) for word in queries)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
        , pattern="FB"
    ), [True, False, True, True, False]],
    [dict(
        queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
        , pattern="FoBa"
    ), [True, False, True, False, False]],
    [dict(
        queries=["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
        , pattern="FoBaT"
    ), [False, True, False, False, False]],
    [dict(queries=["aksvbjLiknuTzqon", "ksvjLimflkpnTzqn", "mmkasvjLiknTxzqn",
                   "ksvjLiurknTzzqbn", "ksvsjLctikgnTzqn", "knzsvzjLiknTszqn"],
          pattern="ksvjLiknTzqn"), [True, True, True, True, True, True]
     ]
    # Expected:[true,true,true,true,true,true]
])
def test_solutions(kw, expected):
    assert Solution().camelMatch(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
