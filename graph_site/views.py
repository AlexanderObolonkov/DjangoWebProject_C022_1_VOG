from os import getenv

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError


class MainView(View):
    def get(self, request, *args, **kwargs):
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
