import django_tables2 as tables
from ..services.math_services import get_nodes


class GraphTable(tables.Table):
    def __init__(self, graph:list[int]):
        print(graph)
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
                if (i, j) in graph or (j,i) in graph:
                    row[j] = 1
                else:
                    row[j] = 0
            data.append(row)

        super().__init__(data)

    class Meta:
        attrs = {"class":"table table-bordered",
                }
        row_attrs = {
                "align":"center"
        }
