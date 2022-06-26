"""
Imagine that a vanquished dragon’s loot is represented as a list of strings like this:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems),
where the inventory parameter is a dictionary representing the player’s inventory
(like in the previous project) and the addedItems parameter is a list like dragonLoot.
The addToInventory() function should return a dictionary that represents the updated inventory.
Note that the addedItems list can contain multiples of the same item.
"""
from chapter05.exercise05_02 import generate_inventory, display_inventory


def generate_dragon_loot():
    _dragon_loot = list()
    _dragon_loot.extend(['scales'] * 60)
    _dragon_loot.extend(['gold'] * 100)
    _dragon_loot.extend(['teeth'] * 50)
    _dragon_loot.extend(['paladin armor'] * 1)
    _dragon_loot.extend(['paladin sword'] * 1)
    _dragon_loot.extend(['paladin rune'] * 1)

    _dragon_loot.extend(['healing potion'] * 10)
    _dragon_loot.extend(['cheese'] * 2)
    return _dragon_loot


def add_to_inventory(_inventory: dict, _loot):
    for _item in _loot:
        _inventory.setdefault(_item, 0)
        _inventory[_item] += 1


if __name__ == '__main__':
    print("\n--- inventory before ---")
    game_inventory = generate_inventory()
    display_inventory(game_inventory)

    print("\n--- dragon loot ---")
    dragon_loot = generate_dragon_loot()
    print(dragon_loot)

    print("\n--- inventory after ---")
    add_to_inventory(game_inventory, dragon_loot)
    display_inventory(game_inventory)
