from django.urls import path
from .views import MainView, BFS_Method

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('bfs_method', BFS_Method.as_view(), name='bfs_method')
]
