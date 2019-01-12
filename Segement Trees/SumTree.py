tree = dict()
data = [2, 3, 4, 5]
data.reverse()


def build(node, start, end):
    if start == end:
        tree[node] = data.pop()
    else:
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build((2 * node) + 1, mid + 1, end)
        tree[node] = tree[(2 * node)] + tree[(2 * node) + 1]


def update(node, index, start, end, val):
    if start == end:
        tree[node] += val
    else:

        mid = (start + end) // 2
        if start <= index <= mid:
            update(2 * node, index, start, mid, val)
        else:
            update((2 * node) + 1, index, mid + 1, end, val)
        tree[node] = tree[(2 * node)] + tree[(2 * node) + 1]


def query(node, start, end, left, right):
    if right < start or left > end:
        return 0

    if start >= left and end <= right:
        return tree[node]

    mid = (start + end) // 2
    s1 = query(2 * node, start, mid, left, right)
    s2 = query((2 * node) + 1, mid + 1, end, left, right)
    return s1 + s2


build(1, 0, 3)
print(tree)
# update(1, 0, 0, 3, 2)
# print(tree)
print(query(1, 0, 3, 1, 3))
