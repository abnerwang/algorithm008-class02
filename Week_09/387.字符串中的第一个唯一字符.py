#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_counts = defaultdict(int)
        for c in s:
            char_counts[c] += 1
        
        for c, ct in char_counts.items():
            if ct == 1:
                return s.index(c)
        
        return -1

# @lc code=end

