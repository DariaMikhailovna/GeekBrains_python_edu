def get_damage(damage, armor):
    return damage / armor


def attack(person1, person2):
    person2['health'] -= get_damage(person1['damage'], person2['armor'])
    person2['health'] = max(person2['health'], 0)


player = {
    'name': input('Get player name: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy = {
    'name': input('Get enemy name: '),
    'health': 100,
    'damage': 50,
    'armor': 1.2
}


# для теста
attack(enemy, player)
print(f'У {player["name"]} осталось {player["health"]} здоровья')
print(f'У {enemy["name"]} осталось {enemy["health"]} здоровья')