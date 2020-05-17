#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
# https://leetcode-cn.com/problems/walking-robot-simulation/description/
#
# algorithms
# Easy (33.65%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    7.8K
# Total Submissions: 22.5K
# Testcase Example:  '[4,-1,3]\n[]'
#
# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：
#
#
# -2：向左转 90 度
# -1：向右转 90 度
# 1 <= x <= 9：向前移动 x 个单位长度
#
#
# 在网格上有一些格子被视为障碍物。
#
# 第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])
#
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。
#
# 返回从原点到机器人的最大欧式距离的平方。
#
#
#
# 示例 1：
#
# 输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#
#
# 示例 2：
#
# 输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#
#
#
#
# 提示：
#
#
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# 答案保证小于 2 ^ 31
#
#
#


# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = 0  # 0: north, 1: east, 2: south 3: west
        obs = set()  #  in order to optimize the query operation
        for obstacle in obstacles:
            obs.add((obstacle[0], obstacle[1]))

        res = 0
        x, y = 0, 0  # initial position

        move_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # corresponding to d
        for command in commands:
            if command == -1:
                d += 1
                if d == 4:  # deal with boundary conditions
                    d = 0
            elif command == -2:
                d -= 1
                if d == -1:  # deal with boundary conditions
                    d = 3
            else:
                while command > 0 and (x + move_dir[d][0],
                                       y + move_dir[d][1]) not in obs:
                    x, y = x + move_dir[d][0], y + move_dir[d][1]
                    command -= 1

            res = max(res, x * x + y * y)  # the Pythagorean theroem

        return res


# @lc code=end
