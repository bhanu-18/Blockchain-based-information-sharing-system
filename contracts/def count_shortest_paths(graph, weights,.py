def count_shortest_paths(graph, weights, source, target, distances, predecessors):
    num_vertices = len(graph)
    
    # Initialize count array
    path_counts = [0] * num_vertices
    path_counts[source] = 1  # There is one shortest path to the source
    
    # Dynamic programming table to store counts
    total_counts = [0] * num_vertices
    total_counts[source] = 1
    
    # Iterate over vertices using the predecessor array
    for vertex in range(num_vertices):
        if predecessors[vertex] is not None:
            for predecessor in predecessors[vertex]:
                if distances[vertex] == distances[predecessor] + weights[(predecessor, vertex)]:
                    path_counts[vertex] += path_counts[predecessor]
                    total_counts[vertex] += total_counts[predecessor]
    
    return total_counts[target]

# Example usage:
graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
weights = {(0, 1): 1, (0, 2): 3, (1, 3): 2, (2, 3): 1}
source_vertex = 0
target_vertex = 3
distances = [0, float('inf'), float('inf'), float('inf')]
predecessors = [None, None, None, None]

# Assign provided values for distances and predecessors
distances = [0, 1, 4, 3]
predecessors = [None, [0], [0], [1, 2]]

# Count the number of shortest paths using dynamic programming
result = count_shortest_paths(graph, weights, source_vertex, target_vertex, distances, predecessors)
print(result)