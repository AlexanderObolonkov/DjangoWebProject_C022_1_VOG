import django_tables2 as tables


class GraphTable(tables.Table):
    name = tables.columns.TemplateColumn(template_code=u"""{{ record.name }}""", orderable=True, verbose_name='Name')
    surname = tables.columns.TemplateColumn(template_code=u"""{{ record.surname }}""", orderable=True, verbose_name='Surname')
    address = tables.columns.TemplateColumn(template_code=u"""{{ record.address }}""", orderable=True, verbose_name='Address')

    class Meta:
        attrs = {'class': 'table table-condensed table-vertical-center', 'id': 'dashboard_table'}
        fields = ('name', 'surname', 'address')
        sequence = fields
        order_by = ('-name', ) 
