学习笔记
---

---

### 递归

若一个问题满足以下三个条件，可以使用递归解决：

1. 一个问题的解可以分解为几个问题的解
2. 这个问题与分解之后的子问题，除了数据规模不同，求解思路完全一样
3. 存在递归终止条件

写递归代码的关键是，写出递推公式，找到终止条件，然后将递推公式转换为代码，**切记莫要人肉递归**。

如果一个问题 A 可以分解为若干子问题 B、C、D，你可以假设子问题 B、C、D 已经解决，在此基础上思考如何解决问题 A。而且，你只需要思考问题 A 与子问题 B、C、D 两层之间的关系即可，不需要一层一层往下思考子问题与子子问题，子子问题与子子子问题之间的关系。

递归代码的模板：

```python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
```

递归代码要警惕堆栈溢出和重复计算的问题。

### 分治

分治算法是一种处理问题的思想，递归是一种编程技巧。分治算法一般都比较适合用递归来实现。

分治算法所能解决的问题，一般需要满足下面几个条件：

- 原问题与分解成的小问题具有相同的模式；
- 原问题分解成的子问题可以独立求解，子问题之间没有相关性，这一点是分治算法与动态规划的明显区别；
- 具有分解终止条件，即问题足够小时，可以直接求解；
- 可以将子问题的解合并成原问题的解，并且合并操作的复杂度不能太高。

分治算法的递归实现中，每一层递归都会涉及以下三个操作：

- 分解：将原问题分解成一系列子问题；
- 解决：递归地求解各个子问题，若子问题足够小，则直接求解；
- 合并：将子问题的结果合并成原问题。

分治算法的代码模板：

```python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
```

