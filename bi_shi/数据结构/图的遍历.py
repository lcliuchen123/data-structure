
# 广度优先遍历bfs:先访问完同一层的结点，然后才继续访问下一层结点，
# 它最有用的性质是可以遍历一次就生成中心结点到所遍历结点的最短路径，这一点在求无权图的最短路径时非常有用。

import queue

def bfs(graph, start):
    q = queue.Queue()
    visited = set()
    q.put(start)
    while not q.empty():
        u = q.get()  # Remove and return an item from the queue.
        print("u: ", u)
        for v in graph.get(u,[]):
            if v not in visited:
                visited.add(v)
                print(visited)
                q.put(v)


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
# bfs(graph, 1)

# 深度优先遍历算法dfs通俗的说就是“顺着起点往下走，直到无路可走就退回去找下一条路径，直到走完所有的结点”
def dfs(graph, start):
    visited = set()
    stack = [[start,0]]
    while stack:
        (v,next_child_index) = stack[-1]
        if (v not in graph) or (next_child_index >= len(graph[v])):
            stack.pop()
            continue
        next_child = graph[v][next_child_index]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child,0])
        print("stack: ", stack)

dfs(graph,1)

# 递归方式实现深度优先遍历
def depthFirstByRecursion(tree, result=[]):
    result.append(tree.data)
    # self.children = []
    children = tree.getChildren()
    for c in children:
        depthFirstByRecursion(c, result)
    return result

# pop: remove and return item at index (default last).
# push：入栈