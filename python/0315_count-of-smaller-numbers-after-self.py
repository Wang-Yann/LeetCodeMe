#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-30 09:41:38
# @Last Modified : 2020-04-30 09:41:38
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于 num
# s[i] 的元素的数量。
#
#
#
#  示例：
#
#  输入：[5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#
#  Related Topics 排序 树状数组 线段树 二分查找 分治算法
#  👍 384 👎 0

"""
注意掌握
#不同
树状数组只能维护前缀“操作和”(前缀和，前缀积，前缀最大最小)，而线段树可以维护区间操作和。
树状数组能做的事情其实是线段树的一个子集，大多数情况下使用树状数组真的只是因为它好写并且常数小而已。
不过随着zkw线段树的普及，树状数组仅有的两点优势也不复存在了

#线段树(segment tree)
空间换时间，用一个变量S保存A[1]到A[n]的和，在Add和Sub操作的时候我们除了对A[i]进行操作外顺便也维护S的值，
这样Add，Sub，Query操作都能在log(n)的时间完成。这个东西就是传说中的线段树

#树状数组 (Binary indexed tree)  (BIT)
在一些实际应用中我们只关心一个数列的前缀和，即只所有的Query都是Query 1 i这种特定类型的Query
给定一个数列A1，A2......，An 以及一堆操作，按顺序执行这些操作。
+ Add i k 操作：Ai += k
+ Sub i K 操作：Ai -= k
+ Query i  操作：输出Ai到Aj的和 sum(i)=A1+....+Ai
用上面所介绍的线段树显然是可以解决这个问题的，而且我们发现由于我们发现二 叉树所有的右孩子去掉后我们仍能
够求出所有的A1+......+Ai，  对于一颗有n个叶节点的完全二叉树T，T共有2n-1个节点，右孩子一共是n-1个，去掉这些
右孩子节点后T刚好是n个节点，
"""
import bisect
from typing import List

import pytest


class Solution:
    """归并排序解法"""

    def countSmaller(self, nums: List[int]) -> List[int]:
        def countAndMergeSort(num_idxs, start, end, counts):
            if end - start <= 0:
                return 0
            mid = (start + end) >> 1
            countAndMergeSort(num_idxs, start, mid, counts)
            countAndMergeSort(num_idxs, mid + 1, end, counts)
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                # Merge the two sorted arrays into tmp.
                while r <= end and num_idxs[r][0] < num_idxs[i][0]:
                    tmp.append(num_idxs[r])
                    r += 1
                tmp.append(num_idxs[i])
                counts[num_idxs[i][1]] += r - (mid + 1)
            num_idxs[start:start + len(tmp)] = tmp

        num_idxs = []
        counts = [0] * len(nums)
        for i, num in enumerate(nums):
            num_idxs.append((num, i))
        countAndMergeSort(num_idxs, 0, len(num_idxs) - 1, counts)
        return counts


class Solution1:
    """https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/solution/bu-dao-10xing-dai-ma-zui-jian-dan-fang-fa-mei-you-/"""

    def countSmaller(self, nums: List[int]) -> List[int]:
        sortns = []
        res = []
        for v in reversed(nums):
            idx = bisect.bisect_left(sortns, v)
            res.append(idx)
            sortns.insert(idx, v)
        print(sortns, res)
        return res[::-1]


class BSTreeNode(object):
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.left = self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def insertNode(self, val):
        node = BSTreeNode(val)
        if not self.root:
            self.root = node
            return
        cur = self.root
        while cur:
            if node.val < cur.val:
                cur.count += 1
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    break
            else:  # Insert right if larger or equal.
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    break

    def query(self, val):
        count = 0
        cur = self.root
        while cur:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                count += cur.count + 1
                cur = cur.right
            else:
                return count + cur.count
        return 0


class Solution2:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        bst = BST()
        for i in range(len(nums) - 1, -1, -1):
            bst.insertNode(nums[i])
            res[i] = bst.query(nums[i])
        return res


@pytest.mark.parametrize("args,expected", [
    ([5, 2, 6, 1], [2, 1, 1, 0]),
    ([1], [0])
])
def test_solutions(args, expected):
    assert Solution().countSmaller(args) == expected
    assert Solution1().countSmaller(args) == expected
    assert Solution2().countSmaller(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", __file__])
