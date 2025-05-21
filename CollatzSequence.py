st_name=input('enter your name')
st_usn=input('enter the usn')
st_sec=input('enter your section')
print('\t\tname:'+st_name)
print('\t\tusn:'+st_usn)
print('\t\tsection:'+st_sec)
print('=====================**********========================')

n=int(input('enter a positive integer'))
while n!=1:
    print(n,end='>')
    if n%2==0:
        n=n//2
    else:
        n=3*n+1

print(1)
