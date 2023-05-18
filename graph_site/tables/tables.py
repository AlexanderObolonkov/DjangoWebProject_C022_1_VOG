import django_tables2 as tables
from ..services.math_services import get_nodes
from django_tables2.export.export import TableExport
import json
import datetime

def check_edge_in_graph(graph,i,j):
    if graph:
        if len(graph[0]) == 2:
            return (i, j) in graph or (j,i) in graph
        elif len(graph[0]) == 3:
            for edge in graph:
                if {i,j} == set(edge[:2]):
                    pass
            return False


class GraphTable(tables.Table):
    def __init__(self, graph:list[int]):
        data = []
        # Получаем все узлы графа
        nodes = get_nodes(graph)
        # Получаем кол-во узлов, чтобы не получать много раз в цикле
        nodes_count = len(nodes)
        self.base_columns["#"] = tables.Column(attrs={"th":{"class":"table-light text-center"}})
                
        for i in nodes:
            self.base_columns[f'{i}'] = tables.Column(attrs={"th":{"class":"table-light text-center"}})
            row = {}
            row["#"] = i           
            for j in nodes:
                if {i,j} in [set(edge[:2]) for edge in graph]:
                    row[j] = 1
                else:
                    row[j] = 0
            data.append(row)
        print([i for i in self.base_columns])
        cur_nodes = []
        for i in list(self.base_columns.keys())[1:]:
            if int(i) not in nodes:
                cur_nodes.append((i, None))
        super().__init__(data, extra_columns=cur_nodes)
        print([i for i in self.base_columns])
        # Экспортирование новосозданной таблички
        export = TableExport('csv', self)
        try:
            json_log = json.load(open("graph_site/logfiles/log.json", 'r'))
        except json.JSONDecodeError:
            json.dump([{"date":datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "content":export.export(), "graph":graph}], open("graph_site/logfiles/log.json", "w"))
        else:
            json_log.append({"date":datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "content":export.export(), "graph":graph})
            json.dump(json_log, open("graph_site/logfiles/log.json", "w"))


    class Meta:
        attrs = {"class":"table table-bordered",
                }
        row_attrs = {
                "align":"center"
        }
