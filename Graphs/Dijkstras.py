import sys


def find_min(distance, visited):
    min_dist = sys.maxsize
    min_ver = None
    for i in range(len(distance)):
        if not visited[i] and distance[i] < min_dist:
            min_dist = distance[i]
            min_ver = i
    return min_ver


def dijkstras(graph, source, distance, visited, parent):
    if source is None:
        return
    visited[source] = True
    for pair in graph[source]:
        if not visited[pair[0]] and distance[source] + pair[1] < distance[pair[0]]:
            distance[pair[0]] = distance[source] + pair[1]
            parent[pair[0]] = source

    min_vertex = find_min(distance, visited)
    return dijkstras(graph, min_vertex, distance, visited, parent)


def print_paths(parent, distance, i):
    if i == len(distance):
        return
    j = i
    print(j, '<--', end=' ')
    while parent[j] != j:
        j = parent[j]
        print(j, '<--', end=' ')
    print('Cost', distance[i])
    return print_paths(parent, distance, i + 1)


if __name__ == '__main__':
    adj_list = {}
    num_vertices = int(input('Enter the number of vertices\n'))
    num_edges = int(input('Enter the number of edges\n'))
    for i in range(num_vertices):
        adj_list[i] = []
    print('Enter edges as a triple\n')
    for i in range(num_edges):
        s, d, w = input().split()
        adj_list[int(s)].append((int(d), int(w)))
        adj_list[int(d)].append((int(s), int(w)))
    source = int(input('Enter the source\n'))
    distance = []
    for i in range(num_vertices):
        distance.append(sys.maxsize)
    distance[source] = 0
    visited = [False for i in range(num_vertices)]
    parent = []
    for i in range(num_vertices):
        parent.append(i)
    dijkstras(adj_list, source, distance, visited, parent)
    print(distance)
    print_paths(parent, distance, 0)
