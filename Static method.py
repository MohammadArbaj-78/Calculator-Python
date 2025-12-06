
# creater static method within class

class main:
    def sum(b):
        return b+b

    @staticmethod
    def cube(a):
       return a*a*a
    
obj=main()
print(obj.cube(2))
print(obj.sum(2))