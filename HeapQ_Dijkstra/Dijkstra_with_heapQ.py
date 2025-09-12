import heapq


def dijkstra(graph_in, start_in):
    # Set all distances to `∞` (infinity)
    dist = {node: float('inf') for node in graph_in}
    # except the source which is `0`
    dist[start_in] = 0
    heap = [(0, start_in)]

    # While the queue is not empty:
    while heap:
        print(dist)
        # pop the head so we can start processing (the head is where the smallest distance is stored)
        current_distance, node = heapq.heappop(heap)

        # For each neighbor
        for neighbor, weight in graph_in[node]:
            # Calculate the potential new distance.
            distance = current_distance + weight
            # If the new distance is smaller, update it and push the neighbor into the queue.
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
        # 3. Repeat until the queue is empty.
    return dist


if __name__ == "__main__":
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('D', 2)],
        'C': [('D', 1)],
        'D': []
    }
    print(dijkstra(graph, "A"))
