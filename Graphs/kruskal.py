# sort the edges
# pick edges greedily
# kruskal algo for connected, undirected graph

class Edge:
    def __init__(self, src, des, weight):
        self.src = src
        self.des = des
        self.weight = weight


def find(v, par):
    if par[v] == v:
        return v

    return find(par[v], par)


# what is important in conversion btwn while loop and recursion is
# what is the condition of while loop -> forms the terminating condition of recursion
# what changes in each while loop along with the condition forms parameters of recursion

def kruskal(num_vertices, edge_list):
    par = []
    for i in range(num_vertices):
        par.append(i)
    count = 0
    i = 0
    cost = 0
    output: list[Edge] = []
    while count != num_vertices - 1:
        edge = edge_list[i]
        par_src = find(edge.src, par)
        par_des = find(edge.des, par)
        if par_src != par_des:
            count += 1
            output.append(edge)
            par[edge.des] = edge.src
            cost += edge.weight
        i += 1

    for edge in output:
        print(vars(edge))
    print('Cost', cost)


if __name__ == '__main__':
    edge_list = list()
    num_vertices = int(input('Enter the number of vertices\n'))
    num_edges = int(input('Enter the number of edges\n'))
    for i in range(num_edges):
        s, d, w = input('Enter edge attributes\n').split()
        edge_list.append(Edge(int(s), int(d), int(w)))
        edge_list.append(Edge(int(d), int(s), int(w)))
    edge_list = sorted(edge_list, key=lambda edge: edge.weight)
    kruskal(num_vertices, edge_list)
