st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')

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
