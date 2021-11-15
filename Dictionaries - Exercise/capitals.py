countries = input().split(", ")
capitals = input().split(", ")

output = {countries[i]: capitals[i] for i in range(len(countries))}

[print(f"{country} -> {capital}") for country, capital in output.items()]
