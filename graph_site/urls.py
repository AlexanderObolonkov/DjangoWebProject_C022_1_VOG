from django.urls import path

from .views import MainView, BFSMethod, KruskalMethod, DFSMethod, Authors

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('bfs_method', BFSMethod.as_view(), name='bfs_method'),
    path('kruskal_method', KruskalMethod.as_view(), name='kruskal'),
    path('dfs_method', DFSMethod.as_view(), name='dfs_method'),
    path('authors', Authors.as_view(), name='authors')
]
