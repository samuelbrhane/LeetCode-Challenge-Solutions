class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        edge_count = {}
        leaves = deque()

        for source, neighbors in adj.items():
            if len(neighbors) == 1:
                leaves.append(source)
            edge_count[source] = len(neighbors)


        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbors in adj[node]:
                    edge_count[neighbors] -= 1
                    if edge_count[neighbors] == 1:
                        leaves.append(neighbors)
        