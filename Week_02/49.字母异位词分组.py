#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
# https://leetcode-cn.com/problems/group-anagrams/description/
#
# algorithms
# Medium (61.21%)
# Likes:    329
# Dislikes: 0
# Total Accepted:    68.5K
# Total Submissions: 111.8K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
#
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# 说明：
#
#
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
#
#
#


# @lc code=start
class Solution:
    # Solution 1
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = []
    #     if not strs:
    #         return res
    #     ascii_diff_str_arr_pair = {}
    #     for s in strs:
    #         seq_diff = [0] * 26
    #         for c in s:
    #             seq_diff[ord(c) - ord('a')] += 1
    #         str_seq_diff = str(seq_diff)
    #         if str_seq_diff in ascii_diff_str_arr_pair:
    #             ascii_diff_str_arr_pair[str_seq_diff].append(s)
    #         else:
    #             ascii_diff_str_arr_pair[str_seq_diff] = [s]
    #     for _, str_arr in ascii_diff_str_arr_pair.items():
    #         res.append(str_arr)

    #     return res

    # Solution 2
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        if not strs:
            return res

        sorted_strs_arr_pair = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sorted_strs_arr_pair:
                sorted_strs_arr_pair[sorted_s].append(s)
            else:
                sorted_strs_arr_pair[sorted_s] = [s]
        for _, str_arr in sorted_strs_arr_pair.items():
            res.append(str_arr)

        return res


# @lc code=end
