import heapq

class Node:
    def __init__(self, name):
        self.name = name
        self.g_score = float('inf')
        self.f_score = float('inf')
        self.parent = None
    
    def __lt__(self, other):
        return self.f_score < other.f_score
    
def a_star(graph, start_node, goal_node):
    open_list = []
    closed_list = set()

    start_node.g_score = 0
    start_node.f_score = heuristic(start_node, goal_node)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node == goal_node:
            return reconstruct_path(current_node)
        
        closed_list.add(current_node)

        for neighbor, cost in graph[current_node.name]:
            neighbor = nodes[neighbor]
            if neighbor in closed_list:
                continue
            tentative_g_score = current_node.g_score + cost

            if tentative_g_score < neighbor.g_score:
                neighbor.parent = current_node
                neighbor.g_score = tentative_g_score
                neighbor.f_score = tentative_g_score + heuristic(neighbor, goal_node)

                if neighbor not in open_list:
                    heapq.heappush(open_list, neighbor)
    return None

def reconstruct_path(current_node):
    path = []
    while current_node:
        path.append(current_node.name)
        current_node = current_node.parent

    return path[::-1]

def heuristic(node, goal_node):
    return 0

if __name__== "__main__":
    graph = {
        'A' : [('B', 4), ('C', 2)],
        'B' : [('C', 5), ('D', 10)],
        'C' : [('D', 3)],
        'D' : []
    }
    
    nodes = {name: Node(name) for name in graph.keys()}
    start_node = nodes['A']
    goal_node = nodes['D']

    path = a_star(graph, start_node, goal_node)

    if path:
        print("Path found: ", path)
    else:
        print("Goal not reachable")