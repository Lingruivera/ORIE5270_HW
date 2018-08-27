import itertools
import heapq


def find_shortestpath(file_name, source, destination):
    data = []
    with open(file_name) as f:
        for line1, line2 in itertools.izip_longest(*[f] * 2):
            data.append((line1.replace("\n", "") + "," + line2.replace("\n", "")))  # .split())

    graph = {}
    for i in range(len(data)):
        record = data[i]
        vertex = record[0]
        if len(record) > 2:
            connected_edge = eval('[' + record[2:] + ']')
        else:
            connected_edge = []
        graph[vertex] = connected_edge

    source = str(source)
    destination = destination
    vertex_set = set([i for i in graph])

    distance = {}
    previous = {}

    for i in vertex_set:
        distance[i] = float("inf")
        previous[i] = None

    distance[source] = 0

    priority_distance = []
    for vertex,dist in distance.items():
        item = [dist,vertex]
        heapq.heappush(priority_distance, item)

    while len(priority_distance) > 0:
        shortest_edge = heapq.heappop(priority_distance)
        vertex = shortest_edge[1]
        dist = shortest_edge[0]
        for neighbor, length in graph[str(vertex)]:
            new_dist = dist + float(length)
            if new_dist < distance[str(neighbor)]:
                distance[str(neighbor)] = new_dist
                previous[str(neighbor)] = vertex
                heapq.heappush(priority_distance, [new_dist, str(neighbor)])

    shortest_path = {}
    for i in vertex_set:
        path = [i]
        prev = previous[i]
        while prev is not None:
            path.insert(0, prev)
            prev = previous[prev]
        if len(path)>1:
            shortest_path[i] = path
        else:
            shortest_path[i] = 'No path found'
    return distance[str(destination)], shortest_path[str(destination)]


if __name__ == '__main__':
    file_name = 'graph.txt'
    source = '1'
    destination = '4'
    res = find_shortestpath(file_name, source, destination)
    print(res)
