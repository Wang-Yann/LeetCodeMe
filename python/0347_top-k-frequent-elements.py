#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。 
#  你可以按任意顺序返回答案。 
#  
#  Related Topics 堆 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """桶排序"""
        counter = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for i, count in counter.items():
            buckets[count].append(i)
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
        return res


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        return [k for k, v in counter.most_common(k)]


@pytest.mark.parametrize("kw,expected", [
    [dict(nums=[1, 1, 1, 2, 2, 3], k=2), [1, 2]],
    [dict(nums=[1], k=1), [1]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().topKFrequent(**kw)) == sorted(expected)
    assert sorted(Solution1().topKFrequent(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
