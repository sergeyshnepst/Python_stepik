"""
Вам доступны списки countries, capitals и population. Используя параллельную итерацию сразу по трем спискам countries, capitals и population, выведите информацию о стране в следующем формате:
"""
#<capital> is the capital of <country>, population equal <population> people.

#Moscow is the capital of Russia, population equal 145934462 people.
#Washington is the capital of USA, population equal 331002651 people.

countries = ['Australia', 'Canada', 'Portugal', 'Japan']
capitals = ['Canberra', 'Ottawa', 'Lissabon', 'Tokyo']
population = [27_840_775, 41_575_585, 10_749_635, 122_950_000]

result = zip(countries, capitals, population)
print(*list(map(lambda info: f"{info[1]} is the capital of {info[0]}, population equal {info[2]} people.", result)), sep="\n")

# Решение от преподавателя через цикл
#for country, capital, population in zip(countries, capitals, population):
#    print(f'{capital} is the capital of {country}, population equal {population} people.')