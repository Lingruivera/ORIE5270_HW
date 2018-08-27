import itertools

def Bellman_Ford(file_name):
    data = []
    with open(file_name) as f:
        for line1, line2 in itertools.izip_longest(*[f] * 2):
            data.append((line1.replace("\n", "") + "," + line2.replace("\n", "")))
    graph = {}

    for i in range(len(data)):
        record = data[i]
        vertex = record[0]
        if len(record) > 2:
            connected_edge = eval('[' + record[2:] + ']')
        else:
            connected_edge = []
        graph[vertex] = connected_edge

    graph['add'] = [(i, 0) for i in graph]

    source = 'add'  # search from the added vertex
    vertex_set = set([i for i in graph])

    distance = {}
    previous = {}

    for i in vertex_set:
        distance[i] = float("inf")
        previous[i] = None

    distance[source] = 0

    edges = []
    for i in graph.items():
        edges.append([(i[0], str(j[0]), j[1]) for j in i[1]])
    edges = [item for sublist in edges for item in sublist]
    
    for i in range(len(vertex_set) - 1):
        for edge in edges:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                previous[v] = u

    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if distance[u] + w < distance[v]:
            distance[v] = distance[u] + w
            previous[v] = u
            path = [v]
            prev = previous[v]
            while len(path) == len(set(path)):
                path.insert(0, prev)
                prev = previous[prev]

            negcircle = [path[0]]
            for j in path[1:]:
                if j != path[0]:
                    negcircle.append(j)
            print negcircle
            break

if __name__ == '__main__':
    file_name = 'graph_negcircle.txt'
    Bellman_Ford(file_name)

