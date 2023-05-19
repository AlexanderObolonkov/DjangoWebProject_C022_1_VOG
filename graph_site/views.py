from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest

from graph_site.services.app_services import post_answer,get_session_checks


class MainView(View):
    """View главной страницы"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для главной страницы"""
        return render(
            request,
            'graph_site/index.html',
            context={
                'nav_bar': 'index',
            }
        )


class BFSMethod(View):
    """View страницы метода обхода в ширину"""

    def get(self, request, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы метода обхода в ширину"""
        graph=get_session_checks(request,False)
        return render(
            request,
            'graph_site/bfs_method.html',
            context={
                'nav_bar': 'bfs_method',
                'graph_str': graph,
                'input_error': request.session.get('input_error', False),
                'file_error': request.session.get('file_error', False),
            }
        )

    def post(self, request, *args, **kwargs) -> HttpResponse:
        """POST-запрос для страницы метода обхода в ширину"""
        return post_answer(request, 'bfs_method')


class KruskalMethod(View):
    """View страницы метода Краскала"""

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы метода Краскала"""
        graph=get_session_checks(request,True)
        return render(
            request,
            'graph_site/kruskal_method.html',
            context={
                'nav_bar': 'kruskal',
                'graph_str': graph,
                'input_error': request.session.get('input_error', False),
                'file_error': request.session.get('file_error', False),
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST-запрос для страницы метода Краскала"""
        return post_answer(request, 'kruskal')


class DFSMethod(View):
    def get(self, request, *args, **kwargs):
        """GET-запрос для страницы метода обхода в глубину"""
        graph=get_session_checks(request,False)
        return render(
            request,
            'graph_site/dfs.html',
            context={
                'nav_bar': 'dfs',
                'graph_str': graph,
                'input_error': request.session.get('input_error', False),
                'file_error': request.session.get('file_error', False),
            }
        )

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        """POST-запрос для страницы метода обхода в глубину"""
        return post_answer(request, 'dfs_method')


class Authors(View):
    """View страницы авторов"""

    def get(self, request, *args, **kwargs) -> HttpResponse:
        """GET-запрос для страницы авторов"""
        return render(
            request,
            'graph_site/authors.html',
        )
