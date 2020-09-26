import time
num = input('Enter binary input:- ')
x =  [int(x) for x in str(num)]
y = len(x)
flag = 1111110  #defining flag as 1111110
s_count = 0  #senders count(for counting number of one's)
send = 1
#-----senders part-----
for i in range(y):
    if(x[i]==1):
        s_count +=1
        if(s_count == 5):
            x.insert(i+1, 0)
    elif(x[i]==0):
        s_count = 0
    else:
        print('Not a Binary Input')
        send = 0
        break
x.insert(0, flag)
x.insert(len(x), flag)
if(send==1):
    print('Encoding Senders Data.....')
    time.sleep(0.5)
    print('Sending Data:-', end=' ')
    for i in x:
        print(i, end='')

#-----receiver part-----
x.remove(flag)
x.pop(len(x)-1)
r_count= 0
for i in range(y):
    if(x[i]==1):
        r_count +=1
        if(r_count == 5):
            x.pop(i+1)
    elif(x[i]==0):
        r_count = 0
print('\n')
if(send==1):
    print('Decoding Receivers Data.....')
    time.sleep(0.5)
    print('Recieved Data:- ', end='')
    for i in x:
        print(i, end='')

