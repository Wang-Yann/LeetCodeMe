#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-12 20:33:45
# @Last Modified : 2020-04-12 20:33:45
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

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
