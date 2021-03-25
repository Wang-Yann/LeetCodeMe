#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换
# 需遵循如下规则： 
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回一个空列表。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# [
#   ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。 
#  Related Topics 广度优先搜索 数组 字符串 回溯算法

"""
import collections
import string
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        def backtrack(path, word):
            if not trace[word]:
                result.append([word] + path)
            else:
                for prev in trace[word]:
                    backtrack([word] + path, prev)

        dictionary = set(wordList)
        result = []
        cur_level = [beginWord]
        visited = {beginWord}
        found = False
        trace = collections.defaultdict(list)
        while cur_level and not found:
            for word in cur_level:
                visited.add(word)
            nex_level = set()
            for word in cur_level:
                for i in range(len(word)):
                    for c in string.ascii_lowercase:
                        candi = word[:i] + c + word[i + 1:]
                        if candi not in visited and candi in dictionary:
                            if candi == endWord:
                                found = True
                            nex_level.add(candi)
                            trace[candi].append(word)
            cur_level = nex_level
        if found:
            backtrack([], endWord)
        return result


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """
    链接：https://leetcode-cn.com/problems/word-ladder-ii/solution/pythonshuang-xiang-bfsdai-ma-jian-duan-gao-xiao-lu/

    """

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)  # 转换为hash实现O(1)的in判断
        if endWord not in wordList:
            return []
        # 分别为答案、用于剪枝的已访问哈希，前向分支和后向分支，当前的前向分支以及后向分支中的路径和的长度
        # 前向路径分支与后向路径分支的字典结构为{结束词：到达该结束词的路径列表}
        res, visited, forward, backward, _len = [], set(), {beginWord:[[beginWord]]}, {endWord:[[endWord]]}, 2
        while forward:
            if len(forward) > len(backward):  # 始终从路径分支较少的一端做BFS
                forward, backward = backward, forward
            tmp = {}  # 存储新的前向分支
            while forward:
                word, paths = forward.popitem()  # 取出路径结束词以及到达它的所有路径
                visited.add(word)  # 记录已访问
                for i in range(len(word)):
                    for a in string.ascii_lowercase:
                        new = word[:i] + a + word[i + 1:]  # 对结束词尝试每一位的置换
                        if new in backward:  # 如果在后向分支列表里发现置换后的词，则路径会和
                            if paths[0][0] == beginWord:  # 前向分支是从beginWord开始的，添加路径会和的笛卡尔积
                                res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                            else:  # 后向分支是从endWord开始的，添加路径会和的笛卡尔积
                                res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                        if new in wordList and new not in visited:  # 仅当wordList存在该词且该词还未碰见过才进行BFS
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):  # res已有答案，且下一次BFS的会和路径长度已超过当前长度，不是最短
                break
            forward = tmp  # 更新前向分支
        return res


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"]

    ),
     [
         ["hit", "hot", "dot", "dog", "cog"],
         ["hit", "hot", "lot", "log", "cog"]
     ]
    ),
    (dict(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log"]
    ),
     []
    ),
])
def test_solutions(kwargs, expected):
    assert sorted(Solution().findLadders(**kwargs)) == expected
    assert sorted(Solution1().findLadders(**kwargs)) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
