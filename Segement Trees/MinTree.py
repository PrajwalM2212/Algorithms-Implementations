data = [2, 1, 4, 3]
tree = {}
data.reverse()
max_element = sorted(data).pop()


def build(node, start, end):
    if start == end:
        tree[node] = data.pop()
    else:
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build((2 * node) + 1, mid + 1, end)
        tree[node] = min(tree[2 * node], tree[(2 * node) + 1])


def update(node, start, end, indx, val):
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if indx <= mid:
            update(2 * node, start, mid, indx, val)
        else:
            update((2 * indx) + 1, mid + 1, end, indx, val)
        tree[node] = min(tree[2 * node], tree[(2 * node) + 1])


def query(node, start, end, left, right):
    if right < start or left > end:
        return max_element
    elif left <= start and right >= end:
        return tree[node]
    else:
        mid = (start + end) // 2
        a = query(node * 2, start, mid, left, right)
        b = query((node * 2) + 1, mid + 1, end, left, right)
        return min(a, b)


build(1, 0, 3)
print(tree)
# update(1, 0, 3, 0, 0)
# print(tree)
print(query(1, 0, 3, 1, 3))
