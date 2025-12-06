
# # Game
# import random

# a=input('enter your answer :')

# b=random.choice(['snak','water','Gun'])

# if(a==b):
#     print('user :',a)
#     print('computer :',b)
#     print('Match drow !')    
# elif(a=='snak' and b=='water'):
#     print('user :',a)
#     print('computer :',b)
#     print('User are winner')
# elif(a=='water' and b=='Gun'):
#     print('user :',a)
#     print('computer :',b)
#     print('User are winner')
# elif(a=='Gun' and b=='snak'):
#     print('user :',a)
#     print('computer :',b)
#     print('User are winner')
# else:
#     print('user :',a)
#     print('computer :',b)
#     print('Computer are winner')

import random

a=input('enter your answer :')

b=random.choice(['snak','water','Gun'])

if(a=='snak' or a=='water' or a=='Gun'):
    print('yes')
else:
    print('no')
