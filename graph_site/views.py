from os import getenv

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.mail import send_mail, BadHeaderError
from django_tables2 import SingleTableView

from BottleWebProject_C022_1_ВОГ import settings
from graph_site.services.app_services import input_to_edges, generate_graph, graph_to_input,load_csv
from graph_site.services.math_services import get_nodes 
from .tables.tables import GraphTable
from pyvis.network import Network


def result(request, active):
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


def csv_post_load(request:HttpRequest,url:str)->HttpResponseRedirect:
    network=Network()
    file=request.FILES['file_path'].read()
    graph=load_csv(file)
    if graph!=[()]:
        nodes=get_nodes(graph)
        network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
        network.add_edges(graph)
        for d in network.get_edges():
            d['title'] = d['width']
        network.save_graph('graph_site/templates/graph_site/pvis_graph_file.html')
    return redirect(url)

class MainView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для главной страницы"""
        return render(
            request,
            'graph_site/index.html',
            context={
                'nav_bar': 'index'
            }
        )


class BFS_Method(SingleTableView):
    def get(self, request, *args, **kwargs):
        try:
            graph = graph_to_input(request.session['graph'])
        except:
            graph = []
        return render(
            request,
            'graph_site/bfs_method.html',
            context={
                'nav_bar': 'bfs_method',
                'graph_str': graph
            }
        )

    def post(self, request, *args, **kwargs):
        if request.POST['value'] == 'decide':
            graph = input_to_edges(request.POST['input_graph'])
            request.session['graph'] = graph
            return result(request, 'bfs_method')
        elif request.POST['value'] == 'visualize':
            graph = input_to_edges(request.POST['input_graph'])
            self.network = Network()
            print(graph)
            if(graph != [()]):
                nodes = get_nodes(graph)
                self.network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
                self.network.add_edges(graph)
            self.network.save_graph('graph_site/templates/graph_site/pvis_graph_file.html')
            print(graph)
            request.session['graph'] = graph
            return redirect('/bfs_method')
        elif reqeust.POST['value'] == 'generate':
            self.network = Network()
            nodes = [1, 2, 3, 4]
            self.network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
            self.network.add_edges(generate_graph(4))
            # self.network.add_edges([(1, 2, 10), (2, 3, 5), (3, 4, 5), (3, 5, 2), (2, 6, 2), (6, 7, 2),
            #                        (6, 8, 2), (6, 9, 2), (6, 10, 2)])
            # network.add_edge(1, 2, value=10, title='10')
            self.network.save_graph('graph_site/templates/graph_site/pvis_graph_file.html')
            return redirect('bfs_method')
        elif request.POST['value'] == 'load':
            return csv_post_load(request,'bfs_method')
        return redirect('/bfs_method')

class KruskalMethod(View):
    network = Network()

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы метода Краскала"""
        return render(
            request,
            'graph_site/kruskal_method.html',
            context={
                'nav_bar': 'kruskal'
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST-запрос для страницы метода Краскала"""
        if request.POST['value'] == 'load':
            return csv_post_load(request,'kruskal')
        else:
            self.network = Network()
            nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            self.network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
            self.network.add_edges(input_to_edges(request.POST['input_graph']))
            # self.network.add_edges([(1, 2, 10), (2, 3, 5), (3, 4, 5), (3, 5, 2), (2, 6, 2), (6, 7, 2),
            #                        (6, 8, 2), (6, 9, 2), (6, 10, 2)])
            # network.add_edge(1, 2, value=10, title='10')
            for d in self.network.get_edges():
                d['title'] = d['width']
            self.network.save_graph('graph_site/templates/graph_site/pvis_graph_file.html')
            return redirect('kruskal')
            # return render(
            #     request,
            #     'graph_site/kruskal_method.html',
            #     context={
            #         'nav_bar': 'kruskal',
            #     }
            # )


class DFS_Method(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'graph_site/dfs.html',
            context={
                'nav_bar': 'dfs'
            }
        )


class Authors(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'graph_site/authors.html',
            context={
                'nav_bar': 'authors'
            }
        )

