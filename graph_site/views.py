from os import getenv

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.mail import send_mail, BadHeaderError
from django_tables2 import SingleTableView


from .tables.tables import GraphTable


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
    table = GraphTable([(1,2), (3,1), (3,4), (5,4), (5,1)])
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'graph_site/bfs_method.html',
            context ={
                'nav_bar': 'bfs_method',
                'table': self.table
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        table = GraphTable(graph)



class KruskalMethod(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы метода Краскала"""
        return render(
            request,
            'graph_site/kruskal_method.html',
            context ={
                'nav_bar': 'kruskal'
            }
        )
   

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
    def get (self,request,*args, **kwargs):
        return render(
            request,
            'graph_site/authors.html',
            context={
                'nav_bar': 'authors'
            }
        )
