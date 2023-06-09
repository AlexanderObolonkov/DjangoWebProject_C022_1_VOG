import csv
import io
import re
from random import randint
from time import sleep
from typing import Type

from django.http import HttpResponseRedirect, HttpRequest, QueryDict
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from pyvis.network import Network

from graph_site.services.math_services import get_nodes, get_neighbors, dfs_algorithm, kruskal_algorithm, bfs_algorithm
from graph_site.tables.tables import GraphTable


def check_length_input_graph(graph: list[tuple[int]], is_kruskal: bool, error: Type[BaseException]) -> None:
    """Функция для проверки введенного графа на соответствие алгоритму решения"""
    for edge in graph:
        if len(edge) != 2 + int(is_kruskal):
            raise error


def input_to_edges(text: str | Type[QueryDict], is_kruskal: bool) -> list[tuple[int]]:
    """Функция для конвертации ввода пользователя к списку кортежей"""
    check_str = " ".join([i.strip() for i in text.split()])
    check_str += " "
    if len(text.split("\r\n")[0].split()) == 2:
        if not (re.fullmatch(r"(\d+ \d+ )+", check_str)):
            raise ValueError
    else:
        if not (re.fullmatch(r"(\d+ \d+ \d+ )+", check_str)):
            raise ValueError
    graph = [tuple(int(j) for j in i.split()) for i in text.split('\n')]
    check_length_input_graph(graph, is_kruskal, ValueError)
    return graph


def graph_to_input(graph: list[tuple[int]]) -> str:
    """Функция для конвертации списка кортежей в пользовательский ввод"""
    graph = [map(str, i) for i in graph]
    return "\n".join([" ".join(i) for i in graph])


def generate_edge_weights(graph: list[tuple[int]]) -> None:
    """Функция для генерации весов ребер для алгоритма Краскала"""
    for i in range(len(graph)):
        edge = list(graph.pop(i))
        edge.append(randint(1, 20))
        graph.insert(i, tuple(edge))


def generate_graph(is_kruskal: bool) -> list[tuple[int]]:
    """Функция для генерации графика"""
    max_value = randint(3, 7)
    graph = []
    max_count_edges = int((max_value ** 2 - max_value) / 2)
    for i in range(randint(max_value - 1, max_count_edges)):
        while True:
            start = randint(1, max_value)
            end = randint(1, max_value)
            if start != end:
                edge = tuple(sorted((start, end)))
                if edge not in graph:
                    break
        graph.append(edge)
    for node in get_nodes(graph):
        if not (len(list(get_neighbors(graph, node)))):
            return generate_graph(is_kruskal)
    if is_kruskal:
        generate_edge_weights(graph)
    return graph


def load_csv(file_string: str, is_kruskal: bool) -> list[tuple[int]]:
    """Функция для парсинга выбранного файла"""
    file_string = bytes.decode(file_string, "utf-8")
    io_string = io.StringIO(file_string)
    graph = list()
    for row in csv.reader(io_string):
        try:
            graph.append(tuple([int(i) for i in row]))
        except TypeError:
            raise IOError
    check_length_input_graph(graph, is_kruskal, IOError)
    return graph


def get_result(request: HttpRequest, active: str, tree: list[tuple[int]]):
    """Функция для перехода на страницу с результатом решения"""
    table = GraphTable(tree)
    return render(
        request,
        'graph_site/result.html',
        context={
            'nav_bar': active,
            'table': table,
        }
    )


def visualize(graph: list[tuple[int]], url: str) -> HttpResponseRedirect:
    """Функция визуализации графика"""
    network = Network()
    if graph != [()]:
        nodes = get_nodes(graph)
        network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
        network.add_edges(graph)
        if len(graph[0]) == 3:
            for d in network.get_edges():
                d['title'] = d['width']
                d['width'] = 1
        network.save_graph('graph_site/templates/graph_site/pvis_graph_file.html')
    sleep(1.5)
    return redirect(url)


def decide(graph: list[tuple[int]], url: str) -> list[tuple[int, int]] | list[tuple[int]]:
    """Функция формирования решения"""
    if url == 'dfs_method':
        return dfs_algorithm(graph, graph[0][0])
    elif url == 'kruskal':
        print(kruskal_algorithm(graph))
        return kruskal_algorithm(graph)
    return bfs_algorithm(graph, graph[0][0])


def post_answer(request: HttpRequest, url: str) -> HttpResponseRedirect:
    """Функция корректного ответа на POST-запрос"""
    try:
        request.session['input_error'] = False
        request.session['file_error'] = False
        if request.POST['value'] == 'decide':
            graph = input_to_edges(request.POST['input_graph'], url == 'kruskal')
            tree = decide(graph, url)
            return get_result(request, url, tree)
        else:
            if request.POST['value'] == 'visualize':
                s = request.POST['input_graph']
                graph = input_to_edges(s, url == 'kruskal')
            elif request.POST['value'] == 'generate':
                graph = generate_graph(url == 'kruskal')
            elif request.POST['value'] == 'load':
                file = request.FILES['file_path'].read()
                graph = load_csv(file, url == 'kruskal')
            request.session['graph'] = graph
            return visualize(graph, url)
    except ValueError:
        request.session['input_error'] = True
    except IOError:
        request.session['file_error'] = True
    except MultiValueDictKeyError:
        request.session['file_error'] = True
    return redirect(url)


def get_session_checks(request: HttpRequest, is_kruskal: bool) -> str:
    """Функция для корректного ответа на GET-запросы в методах решения"""
    try:
        saved_graph = request.session['graph']
        check_length_input_graph(saved_graph, is_kruskal, ValueError)
        return graph_to_input(saved_graph)
    except TypeError:
        return ""
    except KeyError:
        return ""
    except ValueError:
        return ""
