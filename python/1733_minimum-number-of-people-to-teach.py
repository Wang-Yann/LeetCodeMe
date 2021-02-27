#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-27 11:20:09
# @Last Modified : 2021-02-27 11:20:09
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个由 m 个用户组成的社交网络里，我们获取到一些用户之间的好友关系。两个用户之间可以相互沟通的条件是他们都掌握同一门语言。 
# 
#  给你一个整数 n ，数组 languages 和数组 friendships ，它们的含义如下： 
# 
#  
#  总共有 n 种语言，编号从 1 到 n 。 
#  languages[i] 是第 i 位用户掌握的语言集合。 
#  friendships[i] = [ui, vi] 表示 ui 和 vi 为好友关系。 
#  
# 
#  你可以选择 一门 语言并教会一些用户，使得所有好友之间都可以相互沟通。请返回你 最少 需要教会多少名用户。 
# 请注意，好友关系没有传递性，也就是说如果 x 和 y 是好友，且 y 和 z 是好友， x 和 z 不一定是好友。
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# 输出：1
# 解释：你可以选择教用户 1 第二门语言，也可以选择教用户 2 第一门语言。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],
# [2,3]]
# 输出：2
# 解释：教用户 1 和用户 3 第三门语言，需要教 2 名用户。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= n <= 500 
#  languages.length == m 
#  1 <= m <= 500 
#  1 <= languages[i].length <= n 
#  1 <= languages[i][j] <= n 
#  1 <= ui < vi <= languages.length 
#  1 <= friendships.length <= 500 
#  所有的好友关系 (ui, vi) 都是唯一的。 
#  languages[i] 中包含的值互不相同。 
#  
#  Related Topics 贪心算法 数组 
#  👍 8 👎 0
  

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Time O(nmm)
        Space O(mn)
        First, find those who can't communicate with each other.
        Then, find the most popular language among them.
        Then teach that language to the minority who doesn't speak it:
        """
        A = list(map(set, languages))
        not_speak = set(a for i, j in friendships for a in [i, j] if not A[i - 1] & A[j - 1])
        counter = collections.Counter()
        for stu in not_speak:
            # print(collections.Counter(A[stu - 1]))
            counter += collections.Counter(A[stu - 1])
        return 0 if not not_speak else len(not_speak) - max(counter.values())


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        Brute Force
        Time O(nmmn)
        Space O(mn)
         TLE
        """
        A = list(map(set, languages))
        res = N = len(friendships)
        for k in range(1, N + 1):
            teach = set()
            for i, j in friendships:
                if A[i - 1] & A[j - 1]:
                    continue
                if k not in A[i - 1]:
                    teach.add(i)
                if k not in A[j - 1]:
                    teach.add(j)
            res = min(res, len(teach))
        return res


@pytest.mark.parametrize("kw,expected", [
    [dict(n=2, languages=[[1], [2], [1, 2]], friendships=[[1, 2], [1, 3], [2, 3]]), 1],
    [dict(n=3, languages=[[2], [1, 3], [1, 2], [3]], friendships=[[1, 4], [1, 2], [3, 4], [2, 3]]), 2],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, Solution1])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().minimumTeachings(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
