num = input('Enter Binary Input: ')
x =  [int(x) for x in str(num)]
z = len(x)
print('1.Even Parity \n2.Odd Parity')
y = int(input('Enter the option to be performed: '))
s_count = 0  #senders count(for counting number of one's)
if(y==1):
    for i in range(y):
        if (x[i] == 1):
            s_count += 1
    if(s_count % 2 == 0):   #if even number of 1's than inserting 0 in the starting of the data
        x.insert(0, 0)
    else:
        x.insert(0, 1)
elif(y==2):
    for i in range(y):
        if (x[i] == 1):
            s_count += 1
    if(s_count % 2 == 0):
        x.insert(0, 1)
    else:
        x.insert(0, 0)     #if  odd number of 1's than inserting 0 in the starting of the data
else:
    print('Wrong Input')

print('Encoded Senders Data:-',end=''), print(*x)
a = input('Enter Recieved Data(with VRC encoded bit in starting): ')
b = [int(b) for b in str(a)]
if(x == b):
    print('Correct Recieved Data')
else:
    print('Incorrect Recieved Data')



