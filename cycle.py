import networkx as nx


def cycle(n):
    graph = nx.Graph()
    graph.update([(i, (i + 1) % n) for i in range(n)], range(n))

    return graph


c = cycle(5)
print(c.nodes(), c.edges())
