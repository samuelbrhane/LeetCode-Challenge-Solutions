class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = [0] * 101

        for birth, death in logs:
            population[birth - 1950] += 1
            population[death - 1950] -= 1

        max_population = 0
        max_year = 1950
        current_population = 0

        for year in range(101):
            current_population += population[year]
            if current_population > max_population:
                max_population = current_population
                max_year = 1950 + year

        return max_year