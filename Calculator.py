
# eval used calculater
# but eval are dengours

def calc():
    b=input('Calculat :')
    d=eval(b)
    # eval convert string to real code expression
    print(d)

calc()


# function use on calculator

def calcu():
    a=int(input('enter first number :'))
    b=int(input('enter second number :'))
    print('choose opretion number')
    print('1. addition')
    print('2. subtraction')
    print('3. multiplication')
    print('4. division')
    print('5. floor division')
    print('6. exponential')
    
    x=int(input('enter operation number'))
    
    match x:
     case 1:  
      return a+b
     case 2:  
      return a-b
     case 3:  
      return a*b
     case 4:  
      return a/b
     case 5:  
      return a//b
     case 6:  
      return a**b

print(calcu())
