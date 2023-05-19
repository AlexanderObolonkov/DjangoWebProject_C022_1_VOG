from collections import deque
from typing import Generator


def get_neighbors(graph, v) -> Generator[int, None, None]:
    """Функция возвращает список соседей для заданного узла"""
    for i in graph:
        if v in i:
            yield i[0] if i[0] != v else i[1]


def get_nodes(graph: list[tuple[int]]) -> list[int]:
    """Функция возращает список узлов графа из списка ребер графа"""
    return sorted(list(set([i[j] for i in graph for j in range(2)])))


def kruskal_algorithm(graph: list[tuple[int]]) -> list[tuple[int]]:
    """Метод Краскала"""
    sorted_graph = sorted(graph, key=lambda x: x[2])
    connected_vertices = set()
    isolated_groups = {}
    skeleton = []

    for r in sorted_graph:
        if r[0] not in connected_vertices or r[1] not in connected_vertices:
            if r[0] not in connected_vertices and r[1] not in connected_vertices:
                isolated_groups[r[0]] = [r[0], r[1]]
                isolated_groups[r[1]] = isolated_groups[r[0]]
            else:
                if not isolated_groups.get(r[0]):
                    isolated_groups[r[1]].append(r[0])
                    isolated_groups[r[0]] = isolated_groups[r[1]]
                else:
                    isolated_groups[r[0]].append(r[1])
                    isolated_groups[r[1]] = isolated_groups[r[0]]

            skeleton.append(r)
            connected_vertices.add(r[0])
            connected_vertices.add(r[1])

    for r in sorted_graph:
        if r[1] not in isolated_groups[r[0]]:
            skeleton.append(r)
            group = isolated_groups[r[0]]
            isolated_groups[r[0]] += isolated_groups[r[1]]
            isolated_groups[r[1]] += group

    return skeleton


def bfs_algorithm(graph: list[tuple[int]], start: int) -> list[tuple[int]]:
    queue = deque()
    queue.append(start)
    was = {start}
    skeleton = []
    prev = start

    while queue:
        prev = queue.popleft()
        for i in get_neighbors(graph, prev):
            if i not in was:
                queue.append(i)
                was.add(i)
                skeleton.append((prev, i))

    return skeleton


def search_next_node(value: int, visited, tree, graph) -> None:
    for neighbour in list(get_neighbors(graph, value)):
        if neighbour not in visited:
            visited.append(neighbour)
            tree.append((value, neighbour))
            search_next_node(neighbour, visited, tree, graph)


def dfs_algorithm(graph: list[tuple[int]], start_value: int) -> list[tuple[int, int]]:
    visited = [start_value]
    tree = []
    search_next_node(start_value, visited, tree, graph)
    return tree
