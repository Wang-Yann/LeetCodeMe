#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 20:33:45
# @Last Modified : 2020-04-12 20:33:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



"""
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#  示例:
#
#  输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
#  说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
#  提示:
#
#
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#  Related Topics 字典树 回溯算法
#  👍 196 👎 0

"""
from typing import List

from common_utils import TrieNode


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = '#'

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords







    def findWordsMe(self, board: List[List[str]], words: List[str]) -> List[str]:
        def need_walk_pos(i, j, visited):
            return 0 <= i <= m - 1 and 0 <= j <= n - 1 and (i, j) not in visited

        def dfsRecu(trie, pos_x, pox_y, curr_word, visited, cur_idx):
            if not need_walk_pos(pos_x, pox_y, visited):
                return
            pos_char = board[pos_x][pox_y]
            if pos_char not in trie.leaves:
                return
            # curr_word_chars.append(pos_char)
            curr_word += pos_char
            next_trie_node = trie.leaves[pos_char]
            if next_trie_node.is_string:
                result.add(curr_word)
            visited.append((pos_x, pox_y))
            for x, y in [(pos_x, pox_y - 1), (pos_x, pox_y + 1), (pos_x - 1, pox_y), (pos_x + 1, pox_y)]:
            # for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                dfsRecu(next_trie_node, x, y, curr_word, visited, cur_idx + 1)
            visited.pop()
            # curr_word.pop()

        m, n = len(board), len(board[0])
        result = set()
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.leaves:
                    dfsRecu(trie, i, j, "", [], 0)
        return list(result)


if __name__ == '__main__':
    sol = Solution()
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    words = ["oath", "pea", "eat", "rain"]
    # res = sol.findWords(board, words)
    res = sol.findWordsMe(board, words)
    print(res)
