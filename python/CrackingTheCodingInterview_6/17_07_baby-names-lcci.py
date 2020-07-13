#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 23:07:18
# @Last Modified : 2020-07-13 23:07:18
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，例如，John 和 Jon 本质上是相同的名字，但被当成
# 了两个名字公布出来。给定两个列表，一个是名字及对应的频率，另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 
# 是相同的，并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。 
# 
#  在结果列表中，选择字典序最小的名字作为真实名字。 
# 
#  示例： 
# 
#  输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"], sy
# nonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
# 输出：["John(27)","Chris(36)"] 
# 
#  提示： 
# 
#  
#  names.length <= 100000 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 13 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        """
        并查集
        """
        p, d, q = {}, {}, collections.defaultdict(int)
        for s in synonyms:
            a, b = s[1: -1].split(',')
            pa, pb = p.setdefault(a, [a]), p.setdefault(b, [b])
            if pa is not pb:  # 并查集基操，对数组引用进行合并
                pa.extend(pb)
                for c in pb:
                    p[c] = pa
        for name in p:
            d.setdefault(id(p[name]), min(p[name]))  # 取字典序最小名
        for s in names:
            i = s.find('(')
            name, count = s[: i], int(s[i + 1: -1])
            q[name in p and d[id(p[name])] or name] += count  # 未合并过的name单独计数
        return [f'{name}({count})' for name, count in q.items()]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        names=["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"],
        synonyms=["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
    ),
        ["John(27)", "Chris(36)"]]

])
def test_solutions(kwargs, expected):
    assert Solution().trulyMostPopular(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
