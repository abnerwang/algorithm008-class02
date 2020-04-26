#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (59.20%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    93.9K
# Total Submissions: 157.7K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_nums_pairs = {}
        for c_in_s in s:
            alpha_nums_pairs[c_in_s] = alpha_nums_pairs.get(c_in_s, 0) + 1
        for c_in_t in t:
            if c_in_t not in alpha_nums_pairs:
                return False
            alpha_nums_pairs[c_in_t] -= 1
        for _, nums in alpha_nums_pairs.items():
            if nums != 0:
                return False
        return True


# @lc code=end
