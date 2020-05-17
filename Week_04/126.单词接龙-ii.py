#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (31.50%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 30.1K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: []
#
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
#
#

# @lc code=start
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        res, words, layer = [], set(wordList), {}

        if endWord not in words:
            return res

        layer[beginWord] = [[beginWord]]

        while layer:
            candidate_layer = collections.defaultdict(list)
            for word in layer:
                if word == endWord:
                    res.extend(ladder for ladder in layer[word])
                else:
                    word_list = list(word)
                    for i in range(len(word_list)):
                        old_ch = word_list[i]
                        for ch in 'abcdefghijklmnopqrstuvwxyz':
                            word_list[i] = ch
                            new_word = ''.join(word_list)
                            if new_word in words:
                                candidate_layer[new_word] += [
                                    ladder + [new_word]
                                    for ladder in layer[word]
                                ]
                        word_list[i] = old_ch

            words -= set(candidate_layer.keys())
            layer = candidate_layer

        return res


# @lc code=end
