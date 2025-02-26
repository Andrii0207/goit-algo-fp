import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l,
                          y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = add_edges(graph, node.right, pos, x=r,
                              y=y - 1, layer=layer + 1)
    return graph


def insert_heap(root, key):
    nodes = [(root, None, None)]
    while nodes:
        node, parent, direction = nodes.pop(0)
        if not node.left:
            node.left = Node(key)
            break
        elif not node.right:
            node.right = Node(key)
            break
        else:
            nodes.append((node.left, node, "left"))
            nodes.append((node.right, node, "right"))
    heapify(root)


def heapify(node):
    if not node:
        return
    smallest = node
    if node.left and node.left.val < smallest.val:
        smallest = node.left
    if node.right and node.right.val < smallest.val:
        smallest = node.right
    if smallest != node:
        node.val, smallest.val = smallest.val, node.val
        heapify(smallest)


def build_heap(arr):
    if not arr:
        return None
    root = Node(arr[0])
    for key in arr[1:]:
        insert_heap(root, key)
    return root


def draw_heap_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


arr = [0, 4, 5, 10, 1, 3]
heap_root = build_heap(arr)
draw_heap_tree(heap_root)
