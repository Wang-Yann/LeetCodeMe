#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个待查数组 queries ，数组中的元素为 1 到 m 之间的正整数。 请你根据以下规则处理所有待查项 queries[i]（从 i=0 到 i=q
# ueries.length-1）： 
# 
#  
#  一开始，排列 P=[1,2,3,...,m]。 
#  对于当前的 i ，请你找出待查项 queries[i] 在排列 P 中的位置（下标从 0 开始），然后将其从原位置移动到排列 P 的起始位置（即下标为 0
#  处）。注意， queries[i] 在 P 中的位置就是 queries[i] 的查询结果。 
#  
# 
#  请你以数组形式返回待查数组 queries 的查询结果。 
# 
#  
# 
#  示例 1： 
# 
#  输入：queries = [3,1,2,1], m = 5
# 输出：[2,1,2,1] 
# 解释：待查数组 queries 处理如下：
# 对于 i=0: queries[i]=3, P=[1,2,3,4,5], 3 在 P 中的位置是 2，接着我们把 3 移动到 P 的起始位置，得到 P=[3
# ,1,2,4,5] 。
# 对于 i=1: queries[i]=1, P=[3,1,2,4,5], 1 在 P 中的位置是 1，接着我们把 1 移动到 P 的起始位置，得到 P=[1
# ,3,2,4,5] 。 
# 对于 i=2: queries[i]=2, P=[1,3,2,4,5], 2 在 P 中的位置是 2，接着我们把 2 移动到 P 的起始位置，得到 P=[2
# ,1,3,4,5] 。
# 对于 i=3: queries[i]=1, P=[2,1,3,4,5], 1 在 P 中的位置是 1，接着我们把 1 移动到 P 的起始位置，得到 P=[1
# ,2,3,4,5] 。 
# 因此，返回的结果数组为 [2,1,2,1] 。  
#  
# 
#  示例 2： 
# 
#  输入：queries = [4,1,2,2], m = 4
# 输出：[3,1,2,0]
#  
# 
#  示例 3： 
# 
#  输入：queries = [7,5,5,8,3], m = 8
# 输出：[6,5,0,7,5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= m <= 10^3 
#  1 <= queries.length <= m 
#  1 <= queries[i] <= m 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = list(range(1, m + 1))
        ans = []
        for i, num in enumerate(queries):
            p_i = P.index(num)
            ans.append(p_i)
            P.insert(0, P.pop(p_i))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(queries=[3, 1, 2, 1], m=5), [2, 1, 2, 1]],
    [dict(queries=[4, 1, 2, 2], m=4), [3, 1, 2, 0]],
    [dict(queries=[7, 5, 5, 8, 3], m=8), [6, 5, 0, 7, 5]],
])
def test_solutions(kw, expected):
    assert Solution().processQueries(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
