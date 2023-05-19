from collections import deque


def get_neighbors(graph, v):
    """Функция возвращает список соседей для заданного узла"""
    for i in graph:
        if v in i:
            yield i[0] if i[0] != v else i[1]


def get_nodes(graph: list[int, int]):
    """Функция возращает список узлов графа из списка ребер графа"""
    return sorted(list(set([i[j] for i in graph for j in range(2)])))


def kruskal_algorithm(graph: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    sorted_graph = sorted(graph, key=lambda x: x[0])
    connected_vertices = set()  # список соединенных вершин
    isolated_groups = {}  # словарь списка изолированных групп вершин
    skeleton = []  # список ребер остова

    for r in sorted_graph:
        if r[1] not in connected_vertices or r[2] not in connected_vertices:  # проверка для исключения циклов в остове
            if r[1] not in connected_vertices and r[2] not in connected_vertices:  # если обе вершины не соединены, то
                isolated_groups[r[1]] = [r[1], r[2]]  # формируем в словаре ключ с номерами вершин
                isolated_groups[r[2]] = isolated_groups[r[1]]  # и связываем их с одним и тем же списком вершин
            else:  # иначе
                if not isolated_groups.get(r[1]):  # если в словаре нет первой вершины, то
                    isolated_groups[r[2]].append(r[1])  # добавляем в список первую вершину
                    isolated_groups[r[1]] = isolated_groups[r[2]]  # и добавляем ключ с номером первой вершины
                else:
                    isolated_groups[r[1]].append(r[2])  # иначе, все то же самое делаем со второй вершиной
                    isolated_groups[r[2]] = isolated_groups[r[1]]

            skeleton.append(r)  # добавляем ребро в остов
            connected_vertices.add(r[1])  # добавляем вершины в множество U
            connected_vertices.add(r[2])

    for r in sorted_graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[2] not in isolated_groups[r[1]]:  # если вершины принадлежат разным группам, то объединяем
            skeleton.append(r)  # добавляем ребро в остов
            gr1 = isolated_groups[r[1]]
            isolated_groups[r[1]] += isolated_groups[r[2]]  # объединим списки двух групп вершин
            isolated_groups[r[2]] += gr1

    return skeleton


def kruskal_algorithm2(graph: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    sorted_graph = sorted(graph, key=lambda x: x[2])
    connected_vertices = set()  # список соединенных вершин
    isolated_groups = {}  # словарь списка изолированных групп вершин
    skeleton = []  # список ребер остова

    for r in sorted_graph:
        if r[0] not in connected_vertices or r[1] not in connected_vertices:  # проверка для исключения циклов в остове
            if r[0] not in connected_vertices and r[1] not in connected_vertices:  # если обе вершины не соединены, то
                isolated_groups[r[0]] = [r[0], r[1]]  # формируем в словаре ключ с номерами вершин
                isolated_groups[r[1]] = isolated_groups[r[0]]  # и связываем их с одним и тем же списком вершин
            else:  # иначе
                if not isolated_groups.get(r[0]):  # если в словаре нет первой вершины, то
                    isolated_groups[r[1]].append(r[0])  # добавляем в список первую вершину
                    isolated_groups[r[0]] = isolated_groups[r[1]]  # и добавляем ключ с номером первой вершины
                else:
                    isolated_groups[r[0]].append(r[1])  # иначе, все то же самое делаем со второй вершиной
                    isolated_groups[r[1]] = isolated_groups[r[0]]

            skeleton.append(r)  # добавляем ребро в остов
            connected_vertices.add(r[0])  # добавляем вершины в множество соединенных вершин
            connected_vertices.add(r[1])

    for r in sorted_graph:  # проходим по ребрам второй раз и объединяем разрозненные группы вершин
        if r[1] not in isolated_groups[r[0]]:  # если вершины принадлежат разным группам, то объединяем
            skeleton.append(r)  # добавляем ребро в остов
            group = isolated_groups[r[0]]
            isolated_groups[r[0]] += isolated_groups[r[1]]  # объединим списки двух групп вершин
            isolated_groups[r[1]] += group

    return skeleton


def bfs_algoritm(graph: list[tuple[int, int]], start: int) -> list[tuple[int, int]]:
    queue = deque()  # Очередь, в которую заполняются соседи текущего узла
    queue.append(start)  # Добавляем начальный узел в очередь
    was = {start}  # Посещенные узлы
    ostov = []  # Итоговое остовное дерево
    prev = start  # Предыдущий узел

    while queue:
        prev = queue.popleft()  # Удаляем из очереди текущий узел
        # Получаем соседей узла, добавляем их в очередь и добавляем узел в посещенные
        for i in get_neighbors(graph, prev):
            if i not in was:
                queue.append(i)
                was.add(i)
                ostov.append((prev, i))  # Добавляем в остовное дерево ребро

    return ostov


def search_next_node(value, visited, tree, graph):
    for neighbour in list(get_neighbors(graph, value)):
        if neighbour not in visited:
            visited.append(neighbour)
            tree.append((value, neighbour))
            search_next_node(neighbour, visited, tree, graph)


def dfs_algorithm(graph, start_value):
    visited = [start_value]
    tree = []
    search_next_node(start_value, visited, tree, graph)
    return tree