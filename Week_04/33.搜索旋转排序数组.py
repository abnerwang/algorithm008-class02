#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.55%)
# Likes:    584
# Dislikes: 0
# Total Accepted:    91.4K
# Total Submissions: 250K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        len_of_nums = len(nums)
        low, high = 0, len_of_nums - 1

        while low < high:
            mid = (low + high) >> 1
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        # rot_pos = low
        # print(rot_pos)
        # low, high = 0, len_of_nums - 1
        # while low <= high:
        #     mid = (low + high) >> 1
        #     real_mid = (mid + rot_pos) % len_of_nums
        #     if nums[real_mid] == target:
        #         return real_mid
        #     if nums[real_mid] < target:
        #         low = mid + 1
        #     else:
        #         high = mid - 1
        if target == nums[low]:
            return low
        elif target == nums[- 1]:
            return len_of_nums - 1
        elif target > nums[-1]:
            low, high = 0, low - 1
        elif target < nums[-1]:
            low, high = low + 1, len_of_nums - 1

        while low <= high:
            mid = (low + high) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return -1


# @lc code=end
