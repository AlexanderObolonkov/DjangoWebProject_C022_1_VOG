from random import randint

def input_to_edges(text: str) -> list[tuple[int]]:
    graph = [tuple(int(j) for j in i.split()) for i in text.split('\n')]
    return graph

def generate_edge_weights(graph):
    for i in range(len(graph)):
        edge=list(graph.pop(i))
        edge.append(randint(1,20))
        graph.insert(i,tuple(edge))

def generate_graph(max_value,is_kruskal=False):
    graph=[]
    max_count_edges=int((max_value**2-max_value)/2)
    for i in range(randint(max_value-1,max_count_edges)):
        while True:
            start=randint(1,max_value)
            end=randint(1,max_value)
            if (start!=end):
                edge=tuple(sorted((start,end)))
                if edge not in graph:
                    break
        graph.append(edge)
    if is_kruskal:
        generate_edge_weights(graph)
    return graph

if __name__ == '__main__':
    print(input_to_edges('1 2\n'
                         '3 4\n'
                         '5 6\n'
                         '7 8'))
