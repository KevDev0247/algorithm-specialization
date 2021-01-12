import random, copy


def load_graph():
    file = open("D:\\Algorithms-Specialization\\files\\min-cut-graph-integers.txt")
    line = file.read().strip().split("\n")

    graph_dict = {}
    for element in line:
        line_list = list(map(int, element.strip().split("\t")))
        graph_dict[line_list[0]] = line_list[1:]

    return graph_dict


def get_random_edge(graph_dict):
    a = random.choice(list(graph_dict.keys()))
    b = random.choice(graph_dict[a])

    edge = (a, b)
    return edge


def karger_algorithm(graph_dict):
    num = []

    while len(graph_dict) > 2:
        a, b = get_random_edge(graph_dict)
        graph_dict[a].extend(graph_dict[b])

        for c in graph_dict[b]:
            graph_dict[c].remove(b)
            graph_dict[c].append(a)

        while a in graph_dict[a]:
            graph_dict[a].remove(a)

        del graph_dict[b]

    for key in graph_dict:
        num.append(len(graph_dict[key]))

    return num[0]


graph = load_graph()
min_cut = 1000
for i in range(100):
    graph = copy.deepcopy(graph)
    cut = karger_algorithm(graph)
    if cut < min_cut:
        min_cut = cut

print(min_cut)