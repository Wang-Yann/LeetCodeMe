#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 14:58:18
# @Last Modified : 2020-08-05 14:58:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你是个城市规划工作者，手里负责管辖一系列的街区。在这个街区列表中 blocks[i] = t 意味着第 i 个街区需要 t 个单位的时间来建造。 
# 
#  由于一个街区只能由一个工人来完成建造。 
# 
#  所以，一个工人要么需要再召唤一个工人（工人数增加 1）；要么建造完一个街区后回家。这两个决定都需要花费一定的时间。 
# 
#  一个工人再召唤一个工人所花费的时间由整数 split 给出。 
# 
#  注意：如果两个工人同时召唤别的工人，那么他们的行为是并行的，所以时间花费仍然是 split。 
# 
#  最开始的时候只有 一个 工人，请你最后输出建造完所有街区所需要的最少时间。 
# 
#  
# 
#  示例 1： 
# 
#  输入：blocks = [1], split = 1
# 输出：1
# 解释：我们使用 1 个工人在 1 个时间单位内来建完 1 个街区。
#  
# 
#  示例 2： 
# 
#  输入：blocks = [1,2], split = 5
# 输出：7
# 解释：我们用 5 个时间单位将这个工人分裂为 2 个工人，然后指派每个工人分别去建造街区，从而时间花费为 5 + max(1, 2) = 7
#  
# 
#  示例 3： 
# 
#  输入：blocks = [1,2,3], split = 1
# 输出：4
# 解释：
# 将 1 个工人分裂为 2 个工人，然后指派第一个工人去建造最后一个街区，并将第二个工人分裂为 2 个工人。
# 然后，用这两个未分派的工人分别去建造前两个街区。
# 时间花费为 1 + max(3, 1 + max(1, 2)) = 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= blocks.length <= 1000 
#  1 <= blocks[i] <= 10^5 
#  1 <= split <= 100 
#  
#  Related Topics 数学 动态规划 
#  👍 17 👎 0

"""

import heapq
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        """
        贪心
        换一个角度来理解，如果我们不是分裂工人，而是合并街区呢? 上面两个街区的情形中，分裂工人的操作，
        实际上就等价于把这两个街区合并为了一个建造时间为 split+max(blocks[0],blocks[1]) 的新街区。
        经典的Huffman Tree
        https://leetcode-cn.com/problems/minimum-time-to-build-blocks/solution/cong-fen-lie-gong-ren-dao-he-bing-jie-qu-tan-xin-c/
        """
        heapq.heapify(blocks)
        while len(blocks) > 1:
            x, y = heapq.heappop(blocks), heapq.heappop(blocks)
            # print(x,y)
            heapq.heappush(blocks, max(x + split, y + split))
        return blocks[0]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(blocks=[1], split=1), 1],
    [dict(blocks=[1, 2], split=5), 7],
    [dict(blocks=[1, 2, 3], split=1), 4],
])
def test_solutions(kw, expected):
    assert Solution().minBuildTime(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
