class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def get_comp(source):
            q = deque([source])
            comp = set([source])

            while q:
                node = q.popleft()

                for nei in adj[node]:
                    if nei in comp:
                        continue

                    q.append(nei)
                    comp.add(nei)

            return comp


        def longest_path(source):
            q = deque([(source, 1)])
            dist = {source:1}

            while q:
                node, length = q.popleft()

                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] not in (length + 1, length - 1):
                            return -1
                        continue

                    q.append((nei, length + 1))
                    dist[nei] = length + 1
                    visited.add(nei)
                    
            return max(dist.values())


        visited = set()
        result = 0

        for i in range(1, n + 1):
            if i in visited:
                continue

            visited.add(i)
            comp = get_comp(i)

            max_count = 0
            for source in comp:
                length = longest_path(source)
                if length == -1:
                    return -1
                max_count = max(max_count, length)

            result += max_count

        return result

                