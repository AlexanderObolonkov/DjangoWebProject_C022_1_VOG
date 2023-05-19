from django.test import TestCase
from graph_site.services.math_services import kruskal_algorithm


class TestKruskalMethod(TestCase):
    def test_match_dfs_result(self):
        #arrange
        graphs = [
            [(1, 3, 1), (1, 2, 3), (1, 4, 5), (2, 3, 3), (2, 4, 4), (2, 5, 7), (3, 5, 8), (4, 5, 10)],
            [(1, 2, 2), (1, 3, 2), (1, 4, 2), (4, 5, 2), (4, 6, 2), (5, 6, 2)],
            [(1, 2, 1), (1, 3, 3)],
            [(1, 2, 5), (1, 3, 5), (1, 4, 1), (2, 3, 3), (2, 4, 3), (3, 4, 3)],
            [(1, 2, 1), (1, 3, 1), (2, 3, 1), (4, 5, 1), (4, 6, 1), (5, 6, 2)],
        ]
        #act
        results = [
            [(1, 3, 1), (1, 2, 3), (2, 4, 4), (2, 5, 7)],
            [(1, 2, 2), (1, 3, 2), (1, 4, 2), (4, 5, 2), (4, 6, 2)],
            [(1, 2, 1), (1, 3, 3)],
            [(1, 4, 1), (2, 3, 3), (2, 4, 3)],
            [(1, 2, 1), (1, 3, 1), (4, 5, 1), (4, 6, 1)]
                ]
        #assert
        for i in range(len(graphs)):
            self.assertEqual(kruskal_algorithm(graphs[i]), results[i])
