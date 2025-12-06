
# Unit Comverter

print('Welcome User')
print('Choose Unit Type')
print('1. Temperature')
print('2. Weight')
print('3. Distance')

for i in range(10):
 
 type=input('enter type (1-3): ')

 if(type=='1'):
    print('Choose Your need ')
    print('1. Celcius => Fahrenheit')
    print('2. Fahrenheit => Celcius')

    temp=int(input('Enter (1-2) :'))

    if(temp==1):

        c=int(input('Enter Celcius : '))
        print('Convert Celcius to Fahrenheit')
        f=(c*9/5)+32
        print(f'Celcius {c} => Fahrenheit {f}')
        
    elif(temp==2):

        f=int(input('Enter Fahrenheit : '))
        print('Convert Fahrenheit to Celcius')
        c=(f-32)*5/9
        print(f'Fahrenheit {f} => Celcius {c}')

 elif(type=='2'):
    print('Choose Your need ')
    print('1. kG => Pound')
    print('2. Pound => KG')

    temp=int(input('Enter (1-2) :'))

    if(temp==1):

        k=int(input('Enter KG : '))
        print('Convert KG to Pound')
        p=k*2.20462
        print(f'KG {k} => Pound {p}')
        
    elif(temp==2):

        p=int(input('Enter Pound : '))
        print('Convert Pound to KG')
        k=p%2.20462
        print(f'Pound {p} => KG {k}')

 elif(type=='3'):
    print('Choose Your need ')
    print('1. KM => Mile')
    print('2. Mile => KM')

    temp=int(input('Enter (1-2) :'))

    if(temp==1):

        k=int(input('Enter Km : '))
        print('Convert Km to Mile')
        m=k*0.621371
        print(f'KM {k} => Mile {m}')
        
    elif(temp==2):

        m=int(input('Enters Mile : '))
        print('Convert Mile to KM')
        k=m%0.621371
        print(f'Mile {m} => KM {k}')

 else:
    print('Exit')
    break
        