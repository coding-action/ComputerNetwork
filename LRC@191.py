a = int(input('Enter Number of data you want to enter(of 8 Bit each): '))
lists = [[] for i in range(a)]
arr = []
count=0
print('1.Even Parity \n2.Odd Parity')
parity_check = int(input('Enter the option to be performed: '))
for i in range(a):
    b = input('Enter Number'+str(i+1) +' of 8 bit: ')
    lists[i].append(b)
#----Row Parity-----
for i in range(a):
    num = str(*lists[i])
    if(len(num)==8):
        for j in num:
            if(j=='1'):
                count += 1
            elif(j=='0'):
                count += 0
            else:
                print('Wrong')
        if(parity_check==1):
            if(count % 2 ==0):
                num = num + '0'
                count = 0
            else:
                num = num + '1'
                count = 0
        elif(parity_check==2):
            if (count % 2 == 0):
                num = num + '1'
                count = 0
            else:
                num = num + '0'
                count = 0
        else:
            print('Invalid Parity Check Input')

        arr.append(num)
    else:
        print('Wrong Input')
#----Column Parity-----------
c_parity =[]
num1 = ""
for i in range(len(arr[0])):
    parity_sum = 0
    for j in arr:
        parity_sum += int(j[i])
    if(parity_check==1):
        if (parity_sum%2==0):
            num1 += "0"
        else:
            num1 += "1"
    elif(parity_check==2):
        if (parity_sum%2==0):
            num1 += "1"
        else:
            num1 += "0"
    else:
        print('Invalid Parity Check Input')
c_parity.append(num1)
aa = ''.join(c_parity)
arr.append(aa)
print('Encoded Senders Data:-', end=' ')
print(*arr)
#---Recievers Part-----

r = int(input('Enter Reciver Number: '))
r_lists = []
for i in range(r):
    b = input('Enter Number'+str(i+1) +' of 9 bit: ')
    r_lists.append(b)
print('Recieved Data:-', end=' '), print(*r_lists)
if(arr==r_lists):
    print('Correct Recieved Data')
else:
    print('InCorrect Recieved Data')
