st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')

# Dice sides: brain, footprint, shotgun
dice = {
    'green': ['brain', 'brain', 'brain', 'footprint', 'footprint', 'shotgun'],
    'yellow': ['brain', 'brain', 'footprint', 'footprint', 'shotgun', 'shotgun'],
    'red': ['brain', 'footprint', 'footprint', 'shotgun', 'shotgun', 'shotgun']
}

# Dice cup: 6 green, 4 yellow, 3 red
cup = ['green'] * 6 + ['yellow'] * 4 + ['red'] * 3

# Draw 3 random dice
hand = random.sample(cup, 3)

print("Dice colors drawn:", hand)

# Roll each die once
results = [random.choice(dice[color]) for color in hand]

print("Roll results:", results)

# Count brains and shotguns
brains = results.count('brain')
shotguns = results.count('shotgun')

print(f"Brains: {brains}, Shotguns: {shotguns}")
