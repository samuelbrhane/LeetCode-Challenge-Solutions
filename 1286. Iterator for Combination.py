class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.index = 0

        def backtrack(idx, path):
            if len(path) == combinationLength:
                self.combinations.append("".join(path))
                return

            for i in range(idx, len(characters)):
                path.append(characters[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        
    def next(self) -> str:
        if self.index < len(self.combinations):
            self.index += 1
            return self.combinations[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)



# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()