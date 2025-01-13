class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = [0]
        counts = Counter(tiles)

        def backtrack():
            for char in counts:
                if counts[char] == 0:
                    continue

                result[0] += 1

                counts[char] -= 1
                backtrack()
                counts[char] += 1

        backtrack()
        return result[0]