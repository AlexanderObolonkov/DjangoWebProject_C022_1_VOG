from django.test import TestCase
from graph_site.services.math_services import bfs_algorithm


class TestBFSMethod(TestCase):
    def test_match_bfs_result(self):
        # arrange
        gotten_results = [
            bfs_algorithm([(1, 3), (1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)], 1),
            bfs_algorithm([(1, 2), (1, 3), (1, 4), (4, 5), (4, 6), (5, 6)],1),
            bfs_algorithm([(1, 2), (1, 3)],1),
            bfs_algorithm([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)],1),
            bfs_algorithm([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)],1)
        ]
        # expected
        expected_results = [
            [(1, 3), (1, 2), (1, 4), (3, 5)],
            [(1, 2), (1, 3), (1, 4), (4, 5), (4, 6)],
            [(1, 2), (1, 3)],
            [(1, 2), (1, 3), (1, 4)],
            [(1, 2), (1, 3)]
                ]
        # assert
        for ind in range(len(gotten_results)):
            self.assertEqual(gotten_results[ind], expected_results[ind])
