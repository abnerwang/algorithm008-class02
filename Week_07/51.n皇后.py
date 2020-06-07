#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (68.69%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    39.2K
# Total Submissions: 56.5K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
# 提示：
#
#
#
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。（引用自
# 百度百科 - 皇后 ）
#
#
#


# @lc code=start
class Solution:
    def __init__(self):
        self._n = None
        self._res = []
        self._q_idx = None
        self._cache_str = None

    @property
    def saveRes(self):
        cache_row_res = []
        for q_idx in self._q_idx:
            copy_str = self._cache_str
            copy_str = copy_str[:q_idx] + 'Q' + copy_str[q_idx + 1:]
            cache_row_res.append(copy_str)
        self._res.append(cache_row_res)

    def isOK(self, row: int, col: int) -> bool:
        cache_col_left_up = col - 1
        cache_col_right_up = col + 1
        row -= 1
        while row >= 0:
            if self._q_idx[row] == col:
                return False
            if cache_col_left_up >= 0 and self._q_idx[row] == cache_col_left_up:
                return False
            if cache_col_right_up < self._n and self._q_idx[
                    row] == cache_col_right_up:
                return False
            row -= 1
            cache_col_left_up -= 1
            cache_col_right_up += 1
        return True

    def calNQueues(self, row: int):
        if row == self._n:
            self.saveRes
            return
        for col in range(self._n):
            if self.isOK(row, col):
                self._q_idx[row] = col
                self.calNQueues(row + 1)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self._n = n
        self._q_idx = [n for _ in range(n)]
        self._cache_str = "." * n
        self.calNQueues(0)
        return self._res


# @lc code=end
