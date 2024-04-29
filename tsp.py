def nearest_neighbor(graph, start_city):
    num_cities = len(graph)
    unvisited_cities = set(graph.keys())
    unvisited_cities.remove(start_city)
    tour = [start_city]
    current_city = start_city
    while unvisited_cities:
        dist = float('inf')
        nearest_city = ''
        for city in unvisited_cities:
            if dist > graph[current_city][city]:
                dist = graph[current_city][city]
                nearest_city = city
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city
        dist = float('inf')
    tour.append(start_city)
    return tour

def create_graph(graph, num2):
    j =1
    print('enter the pairs of cities and the edge costs: ')
    while j <= num2:
        v1, v2, w = input().split()
        w = int(w)
        if v1 in graph and v2 in graph and v1 != v2 and w>=0:
            graph[v1][v2] = graph[v2][v1] = w
            print('edge added!')
            j +=1
        else:
            print('Enter valid verticles /edge weight')
            continue
    return graph

#to read a graph as input and use it to find TSP tour
graph = {}
i = 1
num1 = int(input('Enter number of cities: '))
print("enter the cities: ")
while i <= num1:
    v = input()
    if v not in graph:
        graph[v] = {}
        i += 1
    else:
        print("Vertex already exists...")
num2 = int(input("enter the number of edges in graph: "))
if num2 > (num1 * (num1 -1)/2):
    print("Number of edges is higher...")
else:
    graph = create_graph(graph, num2)
    print("The graph ", graph)
    start_city = input("Enter the source city: ")
    if start_city in graph:
        tour = nearest_neighbor(graph, start_city)
        print("TSP Tour:", tour)
    else:
        print("Invalid city")
'''
graph = {'A': {'B': 2, 'C': 4, 'D': 1},
          'B':{'A':2,'C':1,'D':3},
          'C':{'A':4,'B': 1, 'D':2},'D':{'A':1,'B':2,'C':2}}
print("The graph: ", graph)
start_city = input('enter the source city: ')
if start_city in graph:
    tour = nearest_neighbor(graph, start_city)
    print('TSP Tour', tour)
else:
    print("Invalid city")'''