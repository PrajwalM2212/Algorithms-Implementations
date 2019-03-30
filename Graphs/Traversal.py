def bfs(graph: dict, q: list, v: dict):
    if len(q) == 0:
        return

    length = len(q)
    for entry in range(length):
        for vertice in graph[q.pop(0)]:
            if not v[vertice]:
                v[vertice] = True
                print(vertice)
                q.append(vertice)

    return bfs(graph, q, v)


def dfs(graph: dict, v: dict, node: int):
    for item in graph[node]:
        if not v[item]:
            v[item] = True
            print(item)
            dfs(graph, v, item)


if __name__ == '__main__':
    adj_list = {}
    visited = {}
    queue = []
    vertices = int(input('Enter the number of vertices'))
    for i in range(0, vertices):
        adj_list[i] = []
        visited[i] = False
    num = int(input('Enter the number of edges'))
    print('Enter edges as pair of vertices')
    while num > 0:
        a = int(input())
        b = int(input())
        adj_list[a].append(b)
        adj_list[b].append(a)
        num -= 1
    queue.append(0)
    visited[0] = True
    # print('BFS')
    # bfs(adj_list, queue, visited)
    print('DFS')
    dfs(adj_list, visited, 0)
