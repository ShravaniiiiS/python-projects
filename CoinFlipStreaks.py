st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print(st_name)
print(st_usn)
print(st_sec)
print('=====================**********========================')
import random

def flip_coin():
    return 'H' if random.randint(0, 1) == 0 else 'T'

# Simulate 100 coin flips
flips = [flip_coin() for _ in range(100)]
print("Flips:")
print(' '.join(flips))

# Count streaks
streak_count = 0
current_streak = 1

for i in range(1, len(flips)):
    if flips[i] == flips[i - 1]:
        current_streak += 1
        if current_streak == 6:
            streak_count += 1
    else:
        current_streak = 1  # Reset streak

print("\nNumber of 6-head or 6-tail streaks:", streak_count)
