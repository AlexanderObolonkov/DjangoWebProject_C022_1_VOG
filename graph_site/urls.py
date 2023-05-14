from django.urls import path
from .views import MainView, BFS_Method, KruskalMethod, DFS_Method,Authors

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('bfs_method', BFS_Method.as_view(), name='bfs_method'),
    path('kruskal_method', KruskalMethod.as_view(), name='kruskal'),
    path('dfs_method',DFS_Method.as_view(),name='dfs_method'),
    path('authors', Authors.as_view(),name='authors')
]
