from django.urls import path
from .views import MainView, BFS_Method, KruskalMethod

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('bfs_method', BFS_Method.as_view(), name='bfs_method'),
    path('kruskal_method', KruskalMethod.as_view(), name='kruskal'),
]
