def input_to_edges(text: str) -> list[tuple[int]]:
    graph = [tuple(int(j) for j in i.split()) for i in text.split('\n')]
    return graph


if __name__ == '__main__':
    print(input_to_edges('1 2\n'
                         '3 4\n'
                         '5 6\n'
                         '7 8'))
