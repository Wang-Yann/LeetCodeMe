#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-10 09:55:27
# @Last Modified : 2020-07-10 09:55:27
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 favoriteCompanies ，其中 favoriteCompanies[i] 是第 i 名用户收藏的公司清单（下标从 0 开始）。 
# 
#  请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标。下标需要按升序排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft
# "],["google","facebook"],["google"],["amazon"]]
# 输出：[0,1,4] 
# 解释：
# favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode",
# "google","facebook"] 的子集。
# favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","f
# acebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
# 其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。
#  
# 
#  示例 2： 
# 
#  输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"
# ],["facebook","google"]]
# 输出：[0,1] 
# 解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcod
# e","google","facebook"] 的子集，因此，答案为 [0,1] 。
#  
# 
#  示例 3： 
# 
#  输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
# 输出：[0,1,2,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= favoriteCompanies.length <= 100 
#  1 <= favoriteCompanies[i].length <= 500 
#  1 <= favoriteCompanies[i][j].length <= 20 
#  favoriteCompanies[i] 中的所有字符串 各不相同 。 
#  用户收藏的公司清单也 各不相同 ，也就是说，即便我们按字母顺序排序每个清单， favoriteCompanies[i] != favoriteCompan
# ies[j] 仍然成立。 
#  所有字符串仅包含小写英文字母。 
#  
#  Related Topics 排序 字符串 
#  👍 8 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        """AC"""
        sorted_data = sorted([(set(x), i) for i, x in enumerate(favoriteCompanies)], key=lambda x: -len(x[0]))
        ans = []
        for i, (set_i, idx) in enumerate(sorted_data):
            if any(set_j > set_i for set_j, _ in sorted_data[:i]):
                continue
            ans.append(idx)
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(favoriteCompanies=[["leetcode", "google", "facebook"], ["google", "microsoft"], ["google", "facebook"],
                             ["google"], ["amazon"]])
        , [0, 1, 4]],
    [dict(favoriteCompanies=[["leetcode", "google", "facebook"], ["leetcode", "amazon"], ["facebook", "google"]])
        , [0, 1]],
    [dict(favoriteCompanies=[["leetcode"], ["google"], ["facebook"], ["amazon"]])
        , [0, 1, 2, 3]],
])
def test_solutions(kw, expected):
    assert Solution().peopleIndexes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
