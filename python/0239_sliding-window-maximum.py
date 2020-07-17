#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-28 18:02:47
# @Last Modified : 2020-04-28 18:02:47
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
#
#
#  返回滑动窗口中的最大值。
#
#
#
#  进阶：
#
#  你能在线性时间复杂度内解决此题吗？
#
#
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  -10^4 <= nums[i] <= 10^4
#  1 <= k <= nums.length
#
#  Related Topics 堆 Sliding Window
#  👍 450 👎 0

import collections
from typing import List

import pytest


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        只保留当前滑动窗口中有的元素的索引
        滑动窗口代码框架
        int left = 0, right = 0;
        while (right < s.size()) {
            window.add(s[right]);
            right++;

            while (valid) {
                window.remove(s[left]);
                left++;
            }
        }
        """
        dq = collections.deque()
        result = []
        for i in range(len(nums)):
            # remove indexes of elements not from sliding window
            if i >= k and dq and dq[0] == i - k:
                dq.popleft()
            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]

            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            # compute max in nums[:k]
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result


class TestSolutions:
    def testmaxSlidingWindow(self):
        kw = dict(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
        assert Solution().maxSlidingWindow(**kw) == [3, 3, 5, 5, 6, 7]

    def testmaxSlidingWindow_1(self):
        kw = dict(nums=[3, 6, 7], k=3)
        assert Solution().maxSlidingWindow(**kw) == [7]


@pytest.mark.parametrize("test_input,expected", [
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
    pytest.param(([1, 3, -1, -3, 5, 3, 6, 7], 3), [42], marks=pytest.mark.xfail),
])
def test_eval(test_input, expected):
    assert Solution().maxSlidingWindow(*test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    pytest.param(dict(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3), [3, 3, 5, 5, 6, 7])
])
def test_eval(test_input, expected):
    assert Solution().maxSlidingWindow(**test_input) == expected


def test_skip():
    pytest.skip("skipping this test")


@pytest.mark.xfail
def test_xpass():
    assert 1 + 1 > 2


if __name__ == '__main__':
    pytest.main(["-q", "-v", "--color=yes", __file__])
    # pytest.main(["-q","-l","-v","--color=yes","--pdb"])
