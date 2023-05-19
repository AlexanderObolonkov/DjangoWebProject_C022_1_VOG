from typing import Type
from unittest import TestCase
from graph_site.services.app_services import input_to_edges, check_length_input_graph


def check_length_wrap(graph: list[tuple[int]], is_kruskal: bool, error: Type[BaseException]) -> bool:
    try:
        check_length_input_graph(graph, is_kruskal, error)
    except error:
        return True
    else:
        return False


class InputAreaTest(TestCase):
    def test_check_length_true(self):
        cases = [
           [ [(1,2), (2, 3), (3,4)], False],
            [ [(1,2,3), (2, 3,1), (3,4,2)], True]
        ]
        for i in cases:
            self.assertTrue(check_length_wrap(i[0], i[1], ValueError))
    def test_check_length_false(self):
        cases = [
            [(1,2), (2,3), (3,4), True],
            [ [(1,2,3), (2, 3,1), (3,4,2)], False],
            [[(1,2), (2,3,4), (3,4)], False],
            [[(1,2), (2,3,4), (3,4)], True],
        ]

        for i in cases:
            self.assertFalse(check_length_wrap(i[0], i[1], ValueError))