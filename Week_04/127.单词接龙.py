#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (40.86%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 90.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
#
#
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
#
#
# 说明:
#
#
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
#
#
# 示例 1:
#
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# 输出: 5
#
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
#
#
# 示例 2:
#
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# 输出: 0
#
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
#
#


# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        begin_set, end_set, visited_words, words = set(), set(), set(), set(
            wordList)  # for O(1) time complexity

        if endWord not in words:
            return 0

        ladder_len = 1

        begin_set.add(beginWord)
        end_set.add(endWord)
        alphabet = list('abcdefghijklmnopqrstuvwxyz')

        while begin_set and end_set:
            # two-end BFS
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set

            candidate_begin = []
            for word in begin_set:
                word_to_list = list(word)
                for i in range(len(word_to_list)):
                    old_ch = word_to_list[i]
                    for ch in alphabet:
                        word_to_list[i] = ch
                        new_word = ''.join(word_to_list)
                        if new_word in end_set:
                            return ladder_len + 1
                        if new_word not in visited_words and new_word in words:
                            candidate_begin.append(new_word)
                            visited_words.add(new_word)
                    word_to_list[i] = old_ch

            begin_set = set(candidate_begin)
            ladder_len += 1

        return 0


# @lc code=end
