from os import getenv

from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django_tables2 import SingleTableView

from BottleWebProject_C022_1_ВОГ import settings
from graph_site.services.app_services import *
from graph_site.services.math_services import get_nodes 

import re
    

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
        return post_answer(request,'bfs_method')

class KruskalMethod(View):
    def get(self, request: HttpRequest, *args, **kwargs):
        """GET-запрос для страницы метода Краскала"""
        try:
            graph = graph_to_input(request.session['graph'])
        except:
            graph = []
        return render(
            request,
            'graph_site/kruskal_method.html',
            context={
                'nav_bar': 'kruskal',
                'graph_str': graph
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        """POST-запрос для страницы метода Краскала"""
        return post_answer(request,'kruskal')


class DFS_Method(View):
    def get(self, request, *args, **kwargs):
        try:
            graph = graph_to_input(request.session['graph'])
        except:
            graph = []
        return render(
            request,
            'graph_site/dfs.html',
            context={
                'nav_bar': 'dfs',
                'graph_str': graph
            }
        )
    def post(self, request: HttpRequest, *args, **kwargs):
        """POST-запрос для страницы метода Краскала"""
        return post_answer(request,'dfs_method')


class Authors(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'graph_site/authors.html',
            context={
                'nav_bar': 'authors'
            }
        )

