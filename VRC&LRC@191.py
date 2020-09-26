import os
print('1.Vertical Redundancy Check (VRC)\n2.Longitudinal Redundancy Check (LRC)')
t = int(input('Enter the option number to be performed: '))
if(t==1):
    os.system('python VRC@191.py')
elif(t==2):
    os.system('python LRC@191.py')
