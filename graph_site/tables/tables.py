import datetime
import json

import django_tables2 as tables
from django_tables2.export.export import TableExport

from ..services.math_services import get_nodes


class GraphTable(tables.Table):
    """Класс таблицы результатов"""

    def __init__(self, graph: list[tuple[int]]):
        data = []
        nodes = get_nodes(graph)
        nodes_count = len(nodes)
        self.base_columns["#"] = tables.Column(attrs={"th": {"class": "table-light text-center"}})

        for i in nodes:
            self.base_columns[f'{i}'] = tables.Column(attrs={"th": {"class": "table-light text-center"}})
            row = {"#": i}
            for j in nodes:
                if {i, j} in [set(edge[:2]) for edge in graph]:
                    row[j] = 1
                else:
                    row[j] = 0
            data.append(row)
        cur_nodes = []
        for i in list(self.base_columns.keys())[1:]:
            if int(i) not in nodes:
                cur_nodes.append((i, None))
        super().__init__(data, extra_columns=cur_nodes)
        export = TableExport('csv', self)
        try:
            json_log = json.load(open("graph_site/logfiles/log.json", 'r'))
        except json.JSONDecodeError:
            json.dump([{"date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "content": export.export(),
                        "graph": graph}], open("graph_site/logfiles/log.json", "w"))
        else:
            json_log.append({"date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"), "content": export.export(),
                             "graph": graph})
            json.dump(json_log, open("graph_site/logfiles/log.json", "w"))

    class Meta:
        attrs = {"class": "table table-bordered w-75", "align": "center"
                 }
        row_attrs = {
            "align": "center"
        }
