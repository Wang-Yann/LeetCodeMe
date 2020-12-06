#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。 
# 
#  如果可以完成上述分割，则返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3
# 3, 4, 5
#  
# 
#  
# 
#  示例 2： 
# 
#  输入: [1,2,3,3,4,4,5,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3, 4, 5
# 3, 4, 5
#  
# 
#  
# 
#  示例 3： 
# 
#  输入: [1,2,3,4,4,5]
# 输出: False
#  
# 
#  
# 
#  提示： 
# 
#  
#  输入的数组长度范围为 [1, 10000] 
#  
# 
#  
#  Related Topics 堆 贪心算法

"""

import collections
import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        字典的键为序列结尾数值，值为结尾为该数值的所有序列长度（以堆存储）。
        更新方式：每遍历一个数，将该数加入能加入的长度最短的序列中，不能加入序列则新建一个序列；然后更新字典
        """
        chains = collections.defaultdict(list)
        for idx, v in enumerate(nums):
            if not chains[v - 1]:
                heapq.heappush(chains[v], 1)
            else:
                min_len = heapq.heappop(chains[v - 1])
                heapq.heappush(chains[v], min_len + 1)
        print(chains)
        for chain in chains.values():
            if chain and chain[0] < 3:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):
    """贪心

    """

    def isPossible(self, nums):
        """
        从最小的数字开始, 假设当前数字为num
        1. 先看看有没有数组以num - 1结尾, 有的话直接把num放过去, 然后以num - 1结尾的数组个数减1, 以num为结尾的数组的个数加1, num的频率减1, 继续下一个数字
        2. 如果以num - 1结尾的数组个数不够了, 说明需要建立新的数组, 就要看num + 1和num + 2是否还有,
            有的话就建立新的数组, 此时多了一个以num + 2结尾的数组, 所以num + 2结尾的数组个数加1, 同时num + 1, num + 2的频率减1, 最后num的频率也减1, 继续...
        3. 以上两点都不满足的话, 说明当前数字放不到任意一个已有的数组末尾, 并且也不能建立新的长度大于等于3的数组了, 返回False
        """
        freq = collections.Counter(nums)
        tails = collections.Counter()

        for num in nums:
            if freq[num] == 0:
                continue

            if tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                tails[num + 2] += 1
            else:
                return False

            freq[num] -= 1

        return True


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 3, 4, 5], True),
    ([1, 2, 3, 3, 4, 4, 5, 5], True),
    ([1, 2, 3, 4, 4, 5], False),
])
def test_solutions(args, expected):
    assert Solution().isPossible(args) == expected
    # assert Solution1().isPossible(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
