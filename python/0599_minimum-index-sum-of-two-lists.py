#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。 
# 
#  你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。 
# 
#  示例 1: 
# 
#  输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# 输出: ["Shogun"]
# 解释: 他们唯一共同喜爱的餐厅是“Shogun”。
#  
# 
#  示例 2: 
# 
#  输入:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# 输出: ["Shogun"]
# 解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。
#  
# 
#  提示: 
# 
#  
#  两个列表的长度范围都在 [1, 1000]内。 
#  两个列表中的字符串的长度将在[1，30]的范围内。 
#  下标从0开始，到列表的长度减1。 
#  两个列表都没有重复的元素。 
#  
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = len(list1) + len(list2)
        ans = []
        for andy in list1:
            if andy in list2:
                idx1 = list1.index(andy)
                idx2 = list2.index(andy)
                if idx1 + idx2 < ans:
                    ans = idx1 + idx2
                    ans = []
                    ans.append(andy)
                elif idx1 + idx2 == ans:
                    ans.append(andy)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map2 = {v: idx for idx, v in enumerate(list2)}
        ans = collections.defaultdict(list)
        for idx, v in enumerate(list1):
            if v in hash_map2:
                ans[idx + hash_map2[v]].append(v)
        return min(ans.items(), key=lambda x: x[0])[1]


@pytest.mark.parametrize("args,expected", [
    (
            (["Shogun", "Tapioca Express", "Burger King", "KFC"],
             ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
             ), ["Shogun"]
    ),
    (
            (
                    ["Shogun", "Tapioca Express", "Burger King", "KFC"],
                    ["KFC", "Shogun", "Burger King"]
            ), ["Shogun"]
    )
])
def test_solutions(args, expected):
    assert Solution().findRestaurant(*args) == expected
    assert Solution1().findRestaurant(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
