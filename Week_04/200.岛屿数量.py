#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (47.88%)
# Likes:    568
# Dislikes: 0
# Total Accepted:    106.2K
# Total Submissions: 214.9K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
#
# 示例 2:
#
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#
#
#


# @lc code=start
class Solution:
    def DFSMarking(self, grid: List[List[str]], row: int, col: int,
                   num_rows: int, num_cols: int):
        if row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[
                row][col] == '0':
            return

        grid[row][col] = '0'
        self.DFSMarking(grid, row - 1, col, num_rows, num_cols)
        self.DFSMarking(grid, row, col + 1, num_rows, num_cols)
        self.DFSMarking(grid, row + 1, col, num_rows, num_cols)
        self.DFSMarking(grid, row, col - 1, num_rows, num_cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        num_rows = len(grid)
        if num_rows == 0:
            return num_islands
        num_cols = len(grid[0])
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    num_islands += 1
                    self.DFSMarking(grid, row, col, num_rows, num_cols)

        return num_islands


# @lc code=end
