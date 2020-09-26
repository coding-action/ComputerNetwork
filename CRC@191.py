y = bin(int(input('Enter key(in binary): '), 2))
key_data = str(y[2:])
x = bin(int(input('Enter Data(in binary): '), 2))
z = str(x[2:])
s = len(str(key_data))-1
input_data = z.ljust(s + len(z), '0')
def xor(p, q):        #defining XOR Function
    result = []
    for i in range(1, len(q)):
        if p[i] == q[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)
#---Sender's side---
get = len(key_data)
temp = input_data[0:get]
while(get < len(input_data)):
    if(temp[0] == '1'):
        temp = xor(key_data,temp) + input_data[get]
    else:  #for temp[0]==0
        temp = xor('0'*get, temp) + input_data[get]           #to substract the data with 0
    get += 1
if temp[0] == '1':
    temp = xor(key_data, temp)
else:
    temp = xor('0' * get, temp)

print('Remainder(XOR division): ' + str(temp))
print('Encoded Data: ',end=' ')
print(str(x[2:]) + str(temp))
s_data = str(x[2:]) + str(temp)
#----receivers side-----
t = bin(int(input('Enter receivers side data: '),2))
r_data = t[2: ]
get = len(key_data)
temp = r_data[0:get]
while(get < len(r_data)):
    if(temp[0] == '1'):
        temp = xor(key_data,temp) + r_data[get]
    else:  #for temp[0]==0
        temp = xor('0'*get, temp) + r_data[get]           #to substract the data with 0
    get += 1
if temp[0] == '1':
    temp = xor(key_data, temp)
else:
    temp = xor('0' * get, temp)
q=''
if(temp== q.ljust(s + len(q), '0')):
    print('Correct Data received')
    print('Reason(Acc. to CRC): Remainder turns out to be ' + str(temp) )
else:
    print('Incorrect Data Received')
    print('Reason(Acc. to CRC): Remainder turns out to be ' + str(temp) + ' which is not equal to zero')
#---Also checking directly with the encoded data---
print('---Direct Check with encoded data---')
if(r_data==s_data):
    print("\033[1m" +"Correct Data received(Matched with encoded data)" + "\033[1m")
else:
    print("\033[1m" +"Incorrect Data Received(Didn't matched with the encoded data)" + "\033[1m")


