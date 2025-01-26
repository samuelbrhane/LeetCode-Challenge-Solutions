class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        longest = 0
        visited = [False] * n
        length_cycle = []

        # Detect cycles
        for i in range(n):
            if visited[i]:
                continue

            curr_set = set()
            curr = i

            while not visited[curr]:
                visited[curr] = True
                curr_set.add(curr)
                curr = favorite[curr]

            if curr in curr_set:
                # Found a cycle
                length = 0
                cycle_start = curr
                while True:
                    length += 1
                    curr = favorite[curr]
                    if curr == cycle_start:
                        break

                longest = max(longest, length)

                # Save mutual favorite pairs (length 2 cycles)
                if length == 2:
                    length_cycle.append([cycle_start, favorite[cycle_start]])

        # Calculate chain lengths for mutual favorite pairs
        def bfs(source, parent):
            q = deque([(source, 0)])
            max_len = 0

            while q:
                node, length = q.popleft()
                max_len = max(max_len, length)

                for neighbor in inverted[node]:
                    if neighbor != parent:
                        q.append((neighbor, length + 1))

            return max_len

        # Build the reverse graph
        inverted = defaultdict(list)
        for i, j in enumerate(favorite):
            inverted[j].append(i)

        # Calculate the total chain length for all mutual favorite pairs
        chain_sum = 0
        for x, y in length_cycle:
            chain_sum += bfs(x, y) + bfs(y, x) + 2

        return max(longest, chain_sum)
