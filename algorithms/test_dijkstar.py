  
from algorithms.dijkstar import dijkstar_shortest_path
import unittest
from collections import defaultdict


class TestDijkstar(unittest.TestCase):

    def setUp(self):
        graph = defaultdict(dict)
        graph['A']['B'] = (2, 1.5)
        graph['A']['C'] = (4, 1.5)
        graph['B']['D'] = (5, 1)
        graph['C']['D'] = (2, 1)
        self.graph = graph

    def test_shortest_path(self):
        self.assertEqual(
            dijkstar_shortest_path(self.graph, 'A', 'D', cost=lambda x: x[0]),
            (6, ['A', 'C', 'D']),
        )

    def test_shortest_path_with_weight(self):
        self.assertEqual(
            dijkstar_shortest_path(self.graph, 'A', 'D', cost=lambda x: x[0] * x[1]),
            (8.0, ['A', 'B', 'D'])
        )

if __name__ == "__main__":
    unittest.main()
