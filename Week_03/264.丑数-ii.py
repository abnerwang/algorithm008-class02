#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (50.92%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    23.2K
# Total Submissions: 45.2K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
#
# 丑数就是只包含质因数 2, 3, 5 的正整数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
#
# 说明:
#
#
# 1 是丑数。
# n 不超过1690。
#
#
#

# @lc code=start
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        heap = []
        heapq.heappush(heap, 1)
        count_n = 0
        nth_ugly_num = None
        while count_n < n:
            nth_ugly_num = heapq.heappop(heap)
            while heap and heap[0] == nth_ugly_num:
                heapq.heappop(heap)
            heapq.heappush(heap, 2 * nth_ugly_num)
            heapq.heappush(heap, 3 * nth_ugly_num)
            heapq.heappush(heap, 5 * nth_ugly_num)
            count_n += 1
        return nth_ugly_num


# @lc code=end
