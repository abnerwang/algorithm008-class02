学习笔记

---

1. 树中容易混淆的三个概念——高度、深度、层：

- 节点的高度 = 节点到叶子节点的 **最长路径**（边数）
- 节点的深度 = 根节点到这个节点所经历的边的个数
- 节点的层数 = 节点的深度 + 1
- 树的高度 = 根节点的高度

2. 二叉树的前、中、后序遍历是一个 **递归过程**，写递归代码的关键是写出递推公式，而写递推公式的关键是，如果要解决问题 A，就假设子问题 B、C 已经解决，然后再来看如何利用 B、C 来解决 A。

3. 二叉查找树删除操作示意图及代码：

   ![](https://res.cloudinary.com/dtfjnb8ft/image/upload/v1587906198/Screen_Shot_2020-04-26_at_8.57.07_PM.png)

   

   代码：

   

   ```python
   
   public void delete(int data) {
     Node p = tree; // p指向要删除的节点，初始化指向根节点
     Node pp = null; // pp记录的是p的父节点
     while (p != null && p.data != data) {
       pp = p;
       if (data > p.data) p = p.right;
       else p = p.left;
     }
     if (p == null) return; // 没有找到
   
     // 要删除的节点有两个子节点
     if (p.left != null && p.right != null) { // 查找右子树中最小节点
       Node minP = p.right;
       Node minPP = p; // minPP表示minP的父节点
       while (minP.left != null) {
         minPP = minP;
         minP = minP.left;
       }
       p.data = minP.data; // 将minP的数据替换到p中
       p = minP; // 下面就变成了删除minP了
       pp = minPP;
     }
   
     // 删除节点是叶子节点或者仅有一个子节点
     Node child; // p的子节点
     if (p.left != null) child = p.left;
     else if (p.right != null) child = p.right;
     else child = null;
   
     if (pp == null) tree = child; // 删除的是根节点
     else if (pp.left == p) pp.left = child;
     else pp.right = child;
   }
   ```

4. 很多时候，在实际的软件开发中，我们在二叉查找树中存储的，是一个包含很多字段的对象。我们利用对象的某个字段作为键值（key）来构建二叉查找树。我们把对象中的其他字段叫作卫星数据。

5. 在二叉查找树中，如果存储的两个对象键值相同，有两种解决办法：

   - 二叉查找树中每一个节点不仅会存储一个数据，因此我们通过链表和支持动态扩容的数组等数据结构，把值相同的数据都存储在同一个节点上。
   - 每个节点仍然只存储一个数据。在查找插入位置的过程中，如果碰到一个节点的值，与要插入数据的值相同，我们就将这个要插入的数据放到这个节点的右子树，也就是说，**把这个新插入的数据当作大于这个节点的值来处理**。当要查找数据的时候，遇到值相同的节点，我们并不停止查找操作，而是继续在右子树中查找，直到遇到叶子节点，才停止。这样就可以把键值等于要查找值的所有节点都找出来。

   

   