from collections import defaultdict, deque
import heapq

def solution(n, paths, gates, summits):
    def low_way():
        heap = [(0, i, i) for i in summits]
        answer = [0, float('inf')]
        visited = [False] * (n+1)
        while heap:
            ity, now, f = heapq.heappop(heap)
            if not visited[now]:
                visited[now] = True
                for next_cost, next_node in m[now]:
                    tmp = max(next_cost, ity)
                    if next_node in gates:
                        if tmp < answer[1]:
                            answer = [f, tmp]
                        elif tmp == answer[1] and f < answer[0]:
                            answer[0] = f
                    if not visited[next_node]:
                        heapq.heappush(heap, (tmp, next_node, f))
        return answer

    gates = set(gates)
    m = defaultdict(list)
    for a, b, c in paths:
        m[a].append((c, b))
        m[b].append((c, a))
    return low_way()

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(
    7,
    [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
    [1],
    [2, 3, 4]

))