
# Create a bank class perform operations

class bank:                                   # Create bank class
    def __init__(self):                       #  Class bank constructer
      self.f=open('c:/Python/pydroid/My projects/bankproject.txt','r')      # Open bank balance file in read mode
      self.r=self.f.read()                    # Assign file data in r variable 
      self.f.close()                          # Close file
      self.amtd=int(self.r)                   # r variable type cast in int and r assign in amtd variable 
      self.f=open('c:/Python/pydroid/My projects/bankpin.txt','r')          # Open bank pin file in read mode
      self.r=self.f.read()                    # Assign file data in r variable 
      self.f.close()                          # Close file
      self.newpin=int(self.r)                 # r variable type cast in int and r assign in newpin variable 
      for self.i in range(100):               # Use for loop range 100
        print('1. deposit')                   
        print('2. withdraw')
        print('3. balance')
        print('4. pinsetup')
        print('Exit')
        ui=int(input('enter your choice in number'))    # Enter Choice number
        if(ui==1):                                      
            self.deposit()                              # Called deposit method 
        elif(ui==2):
            self.withdraw()                             # Called withdraw method
        elif(ui==3):
            self.balance()                              # Called balance method
        elif(ui==4):
            self.pinsetup()                             # Called pinsetup method
        else:
            break                                       # break for exit

class methods(bank):                                    # Create class methods by parent class bank
    def deposit(o):                                     # Deposit method
        o.pins()                                        # Called pins method
        o.amtd+=int(input('enter Deposit Amount :'))    # Enter deposit amount and increment in amtd variable
        o.f=open('c:/Python/pydroid/My projects/bankproject.txt','w')   # Open file in write mode
        o.f.write(str(o.amtd))                          # Write amtd data in file
        o.f.close()                                     # Close file
        print('your amount deposit')
    def withdraw(o):                                    # withdraw method
        o.pins()                                        # Called pins method
        o.amtd-=int(input('enter Withdraw Amount :'))   # Enter deposit amount and dicrement in amtd variable
        o.f=open('c:/Python/pydroid/My projects/bankproject.txt','w')   # Open file in write mode
        o.f.write(str(o.amtd))                          # Write amtd data in file
        o.f.close()                                     # Close file
        print('Please Take your Amount.....')
    def balance(o):                                     # Balance method
        o.pins()                                        # Called pins method
        o.Total()                                       # Called Total method
    def Total(t):                                        
        t.f=open('c:/Python/pydroid/My projects/bankproject.txt','r')    # Open file in read mode
        t.r=t.f.read()                                  # Assign file data in r variable
        t.f.close()                                     # Close file
        print(f'Your Account Balance : {t.r} ')         # Show bank balance
    def pinsetup(o):                                    
        o.pins()                                        # Called pins method
        o.newpin=int(input('enter new pin'))            # Enter new pin and assign in variable
        o.f=open('c:/Python/pydroid/My projects/bankpin.txt','w')        # Open file in write mode
        o.f.write(str(o.newpin))                        # Write newpin in file
        o.f.close()                                     # Close file
        print('your pin set succesfully')
    def pins(p):                                        # pin method
        pin=int(input('enter your pin'))                # Enter pin in pin variable
        if(pin==p.newpin):                              # Check pin by condition statement
            pass 
        else:
            print('your pin is wrong')                  # else statement show wrong pin
            p.pins()                                    # Wrong pin and Called pin methodn enter again write pin

print("Welcome Mohammad Arbaj Bank")                   # Show Bank Name
acc=int(input('Please enter your Account number : '))  # Enter account number
if(acc==12345678912345):                               # Check number by condition statement
     u1=methods()                                      # Create u1 object of methods class
else:                                                  
     print('Invalid account number')                   # Else statement show invelid number
     
     # Exit
