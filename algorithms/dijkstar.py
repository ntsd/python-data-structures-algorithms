import heapq
from typing import Dict, Tuple


def dijkstar_shortest_path(graph: Dict[object, Dict[object, int]], start: object, end: object) -> Tuple:
    """
        Giving: graph{}{} = weight, start, end
        Return: (cost: int, paths: List)
    """
    queue = [(0, start, [])]
    seen = set()
    shortest = (float('inf'), [])
    while True:
        curr_cost, curr, path = heapq.heappop(queue)
        if curr not in seen:
            path = path + [curr]
            seen.add(curr)
            if curr == end:
                if curr_cost < shortest[0]:
                    shortest = (curr_cost, path)
            for next_ in graph[curr]:
                next_cost = curr_cost + graph[curr][next_]
                if next_cost < shortest[0]:
                    heapq.heappush(queue, (next_cost, next_, path))
        if not queue:
            break
    return shortest
