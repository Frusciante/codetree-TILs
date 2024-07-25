n, k = tuple(map(int, input().split()))
stones = list(map(int, input().split()))
middle_stones = stones[1:n-1]

def is_possible(max_val):
    available_indices = []
    for i, stone in enumerate(stones):
        if stone <= max_val:
            available_indices.append(i)
    for j in range(1, len(available_indices)):
        if available_indices[j] - available_indices[j-1] > k:
            return False
    return True

minmax = 100
#중간에 있는 돌들을 각각 최대값이라고 가정하고 순회
for item in middle_stones:
    if is_possible(item):
        minmax = min(minmax, item)

print(item)