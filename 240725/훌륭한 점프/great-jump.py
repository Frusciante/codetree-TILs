n, k = tuple(map(int, input().split()))
stones = list(map(int, input().split()))

def is_possible(max_val):
    available_indices = []
    for i, stone in enumerate(stones):
        if stone <= max_val:
            available_indices.append(i)
    l = len(available_indices)
    if 0 not in available_indices or n - 1 not in available_indices:
        return False
    for j in range(1, l):
        if available_indices[j] - available_indices[j-1] > k:
            return False
    return True

minmax = 100
#중간에 있는 돌들을 각각 최대값이라고 가정하고 순회
for item in stones:
    if is_possible(item):
        minmax = min(minmax, item)

print(minmax)