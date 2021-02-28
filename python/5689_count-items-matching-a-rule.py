#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-28 23:05:13
# @Last Modified : 2021-02-28 23:05:13
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个数组 items ，其中 items[i] = [typei, colori, namei] ，描述第 i 件物品的类型、颜色以及名称。 
# 
#  另给你一条由两个字符串 ruleKey 和 ruleValue 表示的检索规则。 
# 
#  如果第 i 件物品能满足下述条件之一，则认为该物品与给定的检索规则 匹配 ： 
# 
#  
#  ruleKey == "type" 且 ruleValue == typei 。 
#  ruleKey == "color" 且 ruleValue == colori 。 
#  ruleKey == "name" 且 ruleValue == namei 。 
#  
# 
#  统计并返回 匹配检索规则的物品数量 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","
# gold","iphone"]], ruleKey = "color", ruleValue = "silver"
# 输出：1
# 解释：只有一件物品匹配检索规则，这件物品是 ["computer","silver","lenovo"] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","g
# old","iphone"]], ruleKey = "type", ruleValue = "phone"
# 输出：2
# 解释：只有两件物品匹配检索规则，这两件物品分别是 ["phone","blue","pixel"] 和 ["phone","gold","iphone"] 
# 。注意，["computer","silver","phone"] 未匹配检索规则。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= items.length <= 104 
#  1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10 
#  ruleKey 等于 "type"、"color" 或 "name" 
#  所有字符串仅由小写字母组成 
#  
#  Related Topics 数组 字符串 
#  👍 1 👎 0
  

"""

import pytest, traceback
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools

from common_utils import TreeNode, ListNode
from sample_datas import BIG_CASE


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        hash_map = {"type": 0, "color": 1, "name": 2}
        idx = hash_map[ruleKey]
        return sum(x[idx] == ruleValue for x in items)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], ruleKey="color", ruleValue="silver"), 1],
    [dict(items=[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], ruleKey="type", ruleValue="phone"), 2],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().countMatches(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
