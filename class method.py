
# class method

class main:
    name='arbaj'
    
    @classmethod
    def change(cls):
        cls.name='mohammad arbaj'

obj=main()

print(main.name)
obj.change()
print(main.name)