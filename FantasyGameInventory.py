
def add_to_inventory(inventory, loot):
    for item in loot:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

# Example loot from a treasure chest
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'ruby']

# Update inventory
player_inventory = add_to_inventory(player_inventory, dragon_loot)

# Display updated inventory
display_inventory(player_inventory)
