学习笔记

---

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方。

这个题目实际上是一个螺旋排序数组，相当于判断一个螺旋排序数组的旋转点的位置，旋转点所在位置即为无序的地方，寻找旋转点可以使用二分查找法，但是在应用二分查找法的过程中，需要注意的是，如果 `arr[mid] < arr[high]`，那么对 `high` 更新的时候，使用 `high = mid` 而不是 `high = mid + 1`，因为有可能处于 `mid` 位置的数恰好就是旋转点，如果使用 `high = mid + 1` 进行更新的话，有可能就把旋转点错过了。不过，若 `arr[mid] > arr[high]`，则 `low` 的更新方式不变，即 `low = low + 1` 不会导致错过旋转点。另外，在常规的二分查找中，我们需要判断查找到的值是否为我们的目标值，故循环的条件为 `while low <= high`，即我们还需要对  `low == high` 位置的数进行一次判断，但是在寻找螺旋排序数组的旋转点的过程中，则没有这个需求，`low == high` 时，我们已经找到了旋转点。

综上所述，寻找旋转点的代码如下（Python 实现）:

```python
def searchRotatePoint(arr: List[int]) -> int:
    len_of_arr = len(arr)
    low, high = 0, len_of_arr - 1
    while low < high:
        if arr[mid] < arr[high]:
            high = mid
        elif arr[mid] > arr[high]:
            low += 1
    
    return low
```

