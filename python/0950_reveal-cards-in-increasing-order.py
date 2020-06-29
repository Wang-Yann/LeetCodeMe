#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 牌组中的每张卡牌都对应有一个唯一的整数。你可以按你想要的顺序对这套卡片进行排序。 
# 
#  最初，这些卡牌在牌组里是正面朝下的（即，未显示状态）。 
# 
#  现在，重复执行以下步骤，直到显示所有卡牌为止： 
# 
#  
#  从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。 
#  如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。 
#  如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。 
#  
# 
#  返回能以递增顺序显示卡牌的牌组顺序。 
# 
#  答案中的第一张牌被认为处于牌堆顶部。 
# 
#  
# 
#  示例： 
# 
#  输入：[17,13,11,2,3,5,7]
# 输出：[2,13,3,11,5,17,7]
# 解释：
# 我们得到的牌组顺序为 [17,13,11,2,3,5,7]（这个顺序不重要），然后将其重新排序。
# 重新排序后，牌组以 [2,13,3,11,5,17,7] 开始，其中 2 位于牌组的顶部。
# 我们显示 2，然后将 13 移到底部。牌组现在是 [3,11,5,17,7,13]。
# 我们显示 3，并将 11 移到底部。牌组现在是 [5,17,7,13,11]。
# 我们显示 5，然后将 17 移到底部。牌组现在是 [7,13,11,17]。
# 我们显示 7，并将 13 移到底部。牌组现在是 [11,17,13]。
# 我们显示 11，然后将 17 移到底部。牌组现在是 [13,17]。
# 我们展示 13，然后将 17 移到底部。牌组现在是 [17]。
# 我们显示 17。
# 由于所有卡片都是按递增顺序排列显示的，所以答案是正确的。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 1000 
#  1 <= A[i] <= 10^6 
#  对于所有的 i != j，A[i] != A[j] 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
        将所有操作反向进行
        模拟
        0. 将牌组倒序排序，放到手上
        1. 如果结果牌组中有牌，将牌组底部的牌放在牌组的顶部
        2. 将牌放到牌组顶部
        3. 如果手上还有牌，那么返回步骤 1。否则，停止行动。
        https://leetcode-cn.com/problems/reveal-cards-in-increasing-order/solution/ni-cao-zuo-by-iponder/
        """
        dq = collections.deque()
        deck.sort(reverse=True)
        for v in deck:
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(v)
        return list(dq)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [0] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans


@pytest.mark.parametrize("args,expected", [
    ([17, 13, 11, 2, 3, 5, 7], [2, 13, 3, 11, 5, 17, 7])
])
def test_solutions(args, expected):
    assert Solution().deckRevealedIncreasing(args) == expected
    assert Solution1().deckRevealedIncreasing(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
