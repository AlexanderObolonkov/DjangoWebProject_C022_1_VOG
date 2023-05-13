from os import getenv

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.mail import send_mail, BadHeaderError


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


class BFS_Method(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'graph_site/bfs_method.html',
            context={
                'nav_bar': 'index'
            }
        )
<<<<<<< HEAD


class KruskalMethod(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы метода Краскала"""
        return render(
            request,
            'graph_site/kruskal_method.html',
            context={
                'nav_bar': 'kruskal'
            }
        )
=======
    

class DFS_Method(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'graph_site/dfs.html',
            context={
                'nav_bar': 'index'
            }
        )
>>>>>>> 92926cc (Made a transition to the page DFS)
