#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-28 18:02:47
# @Last Modified : 2020-04-28 18:02:47
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
import pytest
import collections
from typing import List


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



sol = Solution()


class TestSolutions:
    def test_maxSlidingWindow(self):
        kw = dict(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
        assert sol.maxSlidingWindow(**kw) == [3, 3, 5, 5, 6, 7]

    def test_maxSlidingWindow_1(self):
        kw = dict(nums=[3, 6, 7], k=3)
        assert sol.maxSlidingWindow(**kw) == [7]


@pytest.mark.parametrize("test_input,expected", [
    (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
    pytest.param(([1, 3, -1, -3, 5, 3, 6, 7], 3), [42], marks=pytest.mark.xfail),
])
def test_eval(test_input, expected):
    assert sol.maxSlidingWindow(*test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    pytest.param(dict(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3),
                 [3, 3, 5, 5, 6, 7])
])
def test_eval(test_input, expected):
    assert sol.maxSlidingWindow(**test_input) == expected


def test_skip():
    pytest.skip("skipping this test")


@pytest.mark.xfail
def test_xpass():
    assert 1 + 1 > 2


if __name__ == '__main__':
    pytest.main(["-q", "-v",  "--color=yes", __file__])
    # pytest.main(["-q","-l","-v","--color=yes","--pdb"])
