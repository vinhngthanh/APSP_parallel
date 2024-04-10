import random
import sys

def generate_random_directed_graph(num_nodes, max_weight=10, probability=0.5):
  graph = [[9000000000000000000] * num_nodes for _ in range(num_nodes)]

  for i in range(num_nodes - 1):
    for j in range(num_nodes):
      if random.random() < probability and i != j:
        weight = random.randint(1, max_weight)
        graph[i][j] = weight

  output = str(num_nodes) + "\n"
  for row in graph:
    output += " ".join([str(val) for val in row]) + "\n"
  return output

num_nodes = 5
graph_string = generate_random_directed_graph(num_nodes)
print(graph_string)
