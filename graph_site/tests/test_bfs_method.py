from django.test import TestCase
from graph_site.services.math_services import bfs_algorithm


class TestBFSMethod(TestCase):
    def test_match_bfs_result(self):
        # arrange
        graphs = [
            [1, [(1, 3), (1, 2), (1, 4), (2, 3), (2, 4), (2, 5), (3, 5), (4, 5)]],
            [1, [(1, 2), (1, 3), (1, 4), (4, 5), (4, 6), (5, 6)]],
            [1, [(1, 2), (1, 3)]],
            [1, [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]],
            [1, [(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)]]
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
        for ind, case_ in enumerate(graphs):
            self.assertEqual(bfs_algorithm(case_[1], case_[0]), expected_results[ind])
