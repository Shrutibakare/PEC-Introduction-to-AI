
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

h = {'A': 4, 'B': 3, 'C': 5, 'D': 3, 'E': 1, 'F': 0}

def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]
            open_list.append((new_f, new_g, neighbor, path + [neighbor]))

    print("Path not found")

astar('A', 'F')
