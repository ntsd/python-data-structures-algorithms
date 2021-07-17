import heapq
from typing import Dict, Tuple, Callable


def dijkstar_shortest_path(
    graph: Dict[object, Dict[object, object]],
    start: object,
    end: object,
    cost: Callable = lambda x: x,
) -> Tuple:
    """
        Dijkstar using BFS
        Parameters:
            graph: {object}{object} = object || int
                graph is 2d dict keys are node and value is cost of it
                Example:
                    graph = {}
                    graph['A'] = {}
                    graph['A']['B'] = 3
                    mean 1 direction graph 'A' to 'B' with cost 3
            start: object
                start node
            end: object
                end node
            cost?: function(x) -> int
                cost function for calculate node cost
        Returns:
            cost: int
            paths: []
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
                    continue
            for next_ in graph[curr]:
                next_cost = curr_cost + cost(graph[curr][next_])
                if next_cost < shortest[0]:
                    heapq.heappush(queue, (next_cost, next_, path))
        if not queue:
            break
    return shortest

if __name__ == '__main__':
    graph = {}
    graph['A'] = {}
    graph['B'] = {}
    graph['C'] = {}
    graph['D'] = {}
    graph['A']['B'] = ([], 2)
    graph['A']['C'] = ([], 4)
    graph['B']['D'] = ([], 5)
    graph['C']['D'] = ([], 2)
    print('shortest path', dijkstar_shortest_path(graph, 'A', 'D', cost=lambda x: -x[1]))
