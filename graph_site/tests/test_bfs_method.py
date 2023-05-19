from unittest import TestCase
from graph_site.services.math_services import bfs_algorithm


class Test(TestCase):
    def test_match_bfs_result(self):
        graphs = [
            [1, [(1, 3), (1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)], [(1, 3), (1, 2), (1, 4), (3, 5)]],
            [1, [(1, 2), (1, 3), (1, 4), (4, 5), (4, 6), (5, 6)], [(1, 2), (1, 3), (1, 4), (4, 5), (4, 6)]],
            [1, [(1, 2), (1, 3)], [(1, 2), (1, 3)]],
            [1, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], [(1, 2), (1, 3), (1, 4)]],
            [1, [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)], [(1, 2), (1, 3)]]
        ]
        for i in graphs:
            self.assertEqual(bfs_algorithm(i[1], i[0]), i[2])
