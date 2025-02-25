import networkx as nx
import matplotlib.pyplot as plt
import random


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = Node(value)
                return
            queue.append(node.left)
            if not node.right:
                node.right = Node(value)
                return
            queue.append(node.right)

    def bfs(self):
        if not self.root:
            return []
        queue, result = [self.root], []

        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        if not self.root:
            return []
        stack, result = [self.root], []

        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


def draw_tree(tree, traversal_order, title):
    G = nx.Graph()
    queue = [(tree.root, None)]
    while queue:
        node, parent = queue.pop(0)
        if parent is not None:
            G.add_edge(parent.value, node.value)
        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))

    pos = nx.spring_layout(G)
    color_map = [f'#{i * 16:02X}00FF' for i in range(len(traversal_order))]
    colors = [color_map[i] for i, _ in enumerate(traversal_order)]

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=colors,
            node_size=1000, font_size=14)
    plt.title(title)
    plt.show()


tree = BinaryTree()

values = [random.randint(1, 99) for _ in range(10)]
for val in values:
    tree.insert(val)

bfs_order = tree.bfs()
dfs_order = tree.dfs()

draw_tree(tree, bfs_order, "BFS")
draw_tree(tree, dfs_order, "DFS")
