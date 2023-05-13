from pyvis.network import Network

network = Network()
nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
network.add_nodes(nodes=nodes, label=[str(i) for i in nodes])
network.add_edges([(1, 2, 10), (2, 3, 5), (3, 4, 5), (3, 5, 2), (2, 6, 2), (6, 7, 2),
                   (6, 8, 2), (6, 9, 2), (6, 10, 2)])
# network.add_edge(1, 2, value=10, title='10')
print(network.get_edges())
for d in network.get_edges():
    d['title'] = d['width']
print(network.get_edges())

# print(network.generate_html())
network.save_graph('name.html')
