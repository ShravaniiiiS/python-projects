st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')
# Ask user for the number
num = int(input("Enter a number to print its multiplication table: "))

print(f"Multiplication table for {num}:")

# Print table from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
