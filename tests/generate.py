import random

def generate_random_directed_graph(num_nodes, max_weight = 10000, probability = 0.7):
  graph = [[1000000000] * num_nodes for _ in range(num_nodes)]

  for i in range(num_nodes):
    for j in range(num_nodes):
      if random.random() < probability and i != j:
        weight = random.randint(1, max_weight)
        graph[i][j] = weight
      if i == j:
        graph[i][j] = 0

  output = str(num_nodes) + "\n"
  for row in graph:
    output += " ".join([str(val) for val in row]) + "\n"
  return output

num_nodes = 2000
graph_string = generate_random_directed_graph(num_nodes)

with open('test6.txt', 'w') as file:
  file.write(graph_string)