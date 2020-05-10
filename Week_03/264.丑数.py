class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count_n = 0
        num = 1
        is_ugly_num = True
        while True:
            i = 2
            while i <= num and is_ugly_num: 
                if num % i == 0 and i not in [1, 2, 3, 5, num]:
                    is_ugly_num = False
                i += 1
            if is_ugly_num:
                count_n += 1
                if count_n == n:
                    return num
            is_ugly_num = True
            num += 1


sol = Solution()
print(sol.nthUglyNumber(7))