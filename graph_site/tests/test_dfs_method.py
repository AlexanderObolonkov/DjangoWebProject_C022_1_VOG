from django.test import TestCase
from graph_site.services.math_services import dfs_algorithm


class Test(TestCase):
    def test_match_dfs_result(self):
        graphs = [
            [1, [(1, 3), (1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)], [(1, 3), (3, 2), (2, 4), (4, 5)]],
            [1, [(1, 2), (1, 3), (1, 4), (4, 5), (4, 6), (5, 6)], [(1, 2), (1, 3), (1, 4), (4, 5), (5, 6)]],
            [1, [(1, 2), (1, 3)], [(1, 2), (1, 3)]],
            [1, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)], [(1, 2), (2, 3), (3, 4)]],
            [1, [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)], [(1, 2), (2, 3)]],
        ]
        for i in graphs:
            self.assertEqual(dfs_algorithm(i[1], i[0]), i[2])
