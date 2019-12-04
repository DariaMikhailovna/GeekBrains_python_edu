def attack(person1, person2):
    person2['health'] -= person1['damage']
    person2['health'] = max(person2['health'], 0)


player = {
    'name': input('Get player name: '),
    'health': 100,
    'damage': 50
}

enemy = {
    'name': input('Get enemy name: '),
    'health': 100,
    'damage': 50
}


# для теста
attack(enemy, player)
print(f'У {player["name"]} осталось {player["health"]} здоровья')
print(f'У {enemy["name"]} осталось {enemy["health"]} здоровья')
