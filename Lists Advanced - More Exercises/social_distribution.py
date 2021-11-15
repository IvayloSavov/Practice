population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

for index, person in enumerate(population):
    if person < minimum_wealth:
        wealthiest_person = max(population)
        wealthiest_person_index = population.index(wealthiest_person)
        if wealthiest_person <= minimum_wealth:
            break
        wealth_to_ad = minimum_wealth - person
        population[index] += wealth_to_ad
        population[wealthiest_person_index] -= wealth_to_ad


not_equal_distribution = [p for p in population if p < minimum_wealth]

if not_equal_distribution:
    print("No equal distribution possible")
else:
    print(population)