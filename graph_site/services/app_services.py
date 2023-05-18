from random import randint
from graph_site.services.math_services import get_neighbors,get_nodes
import csv,io
import re
from graph_site.tables.tables import GraphTable
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from pyvis.network import Network


def input_to_edges(text: str) -> list[tuple[int]]:
    """Функция для конвертации ввода пользователя к списку кортежей"""
    check_str = " ".join([i.strip() for i in text.split()])
    check_str += " "
    if(len(text.split("\r\n")[0].split()) == 2):
        if(re.fullmatch(r"(\d+ \d+ )+", check_str)):
            graph = [tuple(int(j) for j in i.split()) for i in text.split('\n')]
            return graph
        else:
            print(repr(check_str))
            return [()]
    else:
        if(re.fullmatch(r"(\d+ \d+ \d+ )+", check_str)):
            graph = [tuple(int(j) for j in i.split()) for i in text.split('\n')]
            return graph
        else:
            print(repr(check_str))
            return [()]


def graph_to_input(graph: list[tuple[int]]) -> str:
    """Функция для конвертации списка кортежей в пользовательский ввод"""
    graph = [map(str, i) for i in graph]
    return "\n".join([" ".join(i) for i in graph])


def generate_edge_weights(graph:list[tuple[int]])->None:
    """Функция для генерации весов ребер для алгоритма Краскала"""
    for i in range(len(graph)):
        edge=list(graph.pop(i))
        edge.append(randint(1,20))
        graph.insert(i,tuple(edge))

def generate_graph(max_value:int,is_kruskal=False) -> list[tuple[int]]:
    """Функция для генерации графика"""
    graph=[]
    max_count_edges=int((max_value**2-max_value)/2) #Вычисление максимального кол-ва ребер
    for i in range(randint(max_value-1,max_count_edges)):
        while True:
            start=randint(1,max_value)
            end=randint(1,max_value)
            if (start!=end):
                edge=tuple(sorted((start,end)))
                if edge not in graph:
                    break
        graph.append(edge)
    for node in range (1,max_value+1):
        if not(len(list(get_neighbors(graph,node)))):
            return generate_graph(max_value)
    if is_kruskal:
        generate_edge_weights(graph)
    return graph
def load_csv(file_string:str)->list[tuple[int]]:
    """Функция для парсинга выбранного файла"""
    file_string=bytes.decode(file_string,"utf-8")
    io_string = io.StringIO(file_string)
    l=list()
    for row in csv.reader(io_string):
        try:
            l.append(tuple([int(i) for i in row]))
        except:
            return [()]
    return l

def result(request, active):
    """Функция для перехода на страницу с результатом решения"""
    graph = request.session['graph']
    table = GraphTable(graph)
    return render(
            request,
            'graph_site/result.html',
            context={
                'nav_bar': active,
                'table': table
            }
        )

def visualize(graph:list[tuple[int]],url:str)->HttpResponseRedirect:
    """Функция визуализации графика"""
    network=Network()
    if graph!=[()]:
        nodes=get_nodes(graph)
        network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
        network.add_edges(graph)
        for d in network.get_edges():
            d['title'] = d['width']
        network.save_graph('graph_site/templates/graph_site/pvis_graph_file.html')
    return redirect(url)

def csv_post_load(request:HttpRequest,url:str)->HttpResponseRedirect:
    """Функция загрузки и визуализации файла"""
    file=request.FILES['file_path'].read()
    graph=load_csv(file)
    return visualize(graph,url)

if __name__ == '__main__':
    print(input_to_edges('1 2\n'
                         '3 4\n'
                         '5 6\n'
                         '7 8'))
