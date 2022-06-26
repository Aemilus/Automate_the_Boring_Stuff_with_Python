"""
You are creating a fantasy video game.
The data structure to model the player’s inventory will be a dictionary
where the keys are string values describing the item in the inventory
and the value is an integer value detailing how many of that item the player has.

For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function that would take any possible “inventory” and display it like the following:
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
"""


def generate_inventory():
    return {
        'cheese': 2,
        'torch': 4,
        '1H sword': 1,
        'shield': 1,
        'healing potion': 15,
    }


def display_inventory(_inventory: dict):
    _total = 0
    print('Inventory:')
    for k, v in _inventory.items():
        _total += v
        print(f"{k:<15}{v:>10}")
    print(f"\nTotal items: {_total}")


if __name__ == '__main__':
    print("\n--- inventory dict ---")
    game_inventory = generate_inventory()

    print("\n--- display inventory ---")
    display_inventory(game_inventory)
