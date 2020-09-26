import time
y =  input('Enter a String:- ')
flag = '@' #defining flag
esc = '$'  #defining esc
x = list(y)
arr=[]
#---senders part-----
for i in x:
    if(i != flag):
        arr.append(i)
    else:
        arr.append(esc)
        arr.append(i)
q = len(arr)
arr.insert(0, flag)
arr.insert(q+1, flag)
print('Encoding Senders Data....')
time.sleep(0.5)
print('Sending Data:-', end=' ')
for i  in range(len(arr)):
    print(arr[i], end='')

#----receiver part-----
arr.pop(0)
arr.pop(len(arr)-1)

for i in arr:
    if(i == esc):
        arr.remove('$')
print('\n')
print('Decoding Senders Data....')
time.sleep(0.5)
print('Recieved Data:-', end=' ')
for i  in range(len(arr)):
    print(arr[i], end='')