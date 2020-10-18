学习笔记
这周主要学习了字典树、并查集、剪枝搜索、双向BFS、启发式搜索(A* Search)以及AVL树和红黑树
字典树:
    字典树，即Trie树，是一种树形结构的数据结构，将单词的每个字母加入到字典树中，生成出一条路径，
    在搜索时由于有路径的存在，可以有效减少不必要的搜索(类似于剪枝)，并且由于路径的存在，所以某
    个节点即为该节点后所有子树的前缀字符。字典树代码模板如下
    ```
    class Trie(object):
    def __init__(self):
        self.root = {}
        self.eow = '#'

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.eow] = self.eow

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.eow in node

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
    ```

并查集:
    并查集常用于解决快速判断某几个元素是否属于相同集合的问题，例如解决朋友圈的问题，首先，
    初始化并查集，生成一个数组，并将数组中每个元素的领头元素设置为自己，然后通过遍历数组，
    将具有相同性质的元素合并到一起(如将B的领头元素设置为A),最后可以通过压缩路径的方法，大大
    减少查询某个元素的领头元素的搜索时间，经过处理后，就能在并查集中快速判断某几个元素是否
    属于相同的集合。并查集代码模板如下:
    ```
    def init(p):
        p = [i for i in range(n)]

    def union(self, p, i, j): 
        p1 = self.parent(p, i) 
        p2 = self.parent(p, j) 
        p[p1] = p2 
 
    def parent(self, p, i): 
        root = i 
        while p[root] != root: 
            root = p[root]
        # 路径压缩
        while p[i] != i: 
            x = i
            i = p[i]
            p[x] = root 
        return root
    ```

剪枝搜索:
    剪枝搜索的目的是通过预先通过某些判断，在搜索时减少不必要的重复搜索，从而大大提升搜索
    的效率，比如在解决N皇后的问题时，可以通过预先判断某个位置是否已出现在行、列、撇、捺
    这四种集合中，如果出现过，则跳过这个位置，这样就能避免重复搜索,判断如下:
    ```
    for col in range(n):
        if col not in queenlist and row + col not in pie and row - col not in na:
            helper(queenlist + [col], pie + [row + col], na + [row - col])
    ```

双向BFS搜索:
    双向BFS搜索是在BFS搜索的基础上的优化，即从两端开始搜索。单向BFS搜索时，从某一端开始，
    遍历该层中所有的节点，若遇到目标节点则返回层数，否则将该节点的子节点加入到下一层节点中，
    并且层数+1。而双向BFS的层数计算则是分为前段层数和后端层数，当遇到目标节点后，返回的结果
    为前端层数+后端层数。

启发式搜索:
    启发式搜索又称为A* Search，既不是深度优先搜索也不是广度优先搜索，而是优先级优先搜索，
    每次从优先级队列中选出优先级最高的元素，然后对该元素进行搜索。元素的优先级通过估价函数进行
    设置，所以启发式搜索的关键在于找到较好的估价函数。启发式搜索相对于DFS和BFS更加智能，在
    估价函数得当的情况下能更快的找到目标元素。

AVL及红黑树:
    AVL及红黑树都是平衡二叉树，由于二叉树在极端情况下回退化成单链表，时间复杂度退化为O(n),所以
    在每次插入或删除节点时，需要对二叉树做平衡处理。
    AVL:
        计算某个节点左右子树的层数差，得出平衡因子(取值范围为:-1, 0, 1)，通过对平衡因子的判断，
        并以及左旋、右旋、左右旋、右左旋的操作，维持二叉树的平衡性。
    红黑树:
        从根到叶子的最长可能路径不多于最短可能路径的两倍。特性如下:
        1.每个节点要么是红色，要么是黑色
        2.根节点是黑色
        3.每个叶子节点为空节点且为黑色
        4.不能有相邻的红色节点
        5.从任意节点到其每个叶子节点的所有路径都包含相同数目的黑色节点
    AVL与红黑树之间的比较:
        优点:
        由于AVL有平衡因子的存在，所以是严格的二叉平衡树，在查询效率上要比红黑树快，时间复杂度为O(log2N)
        缺点:
        在节点的删除和插入效率上，AVL不及红黑树，这是由于在插入删除元素时AVL需要更多的旋转操作。
        由于平衡因子的存在，AVL占用的空间更多，通常需要一个int来表示平衡因子，而红黑树只需要一个bit就能存储
        节点的类型(红或黑),所以红黑树更多的运用于数据库中


