
# class 

class main:
    class_variable=0
    print(class_variable)

    def __init__(obj):
        main.class_variable+=1
        # print('class_variable',main.class_variable)
    def print_class_variable(obj):
        pass
emp1=main()
emp2=main()
emp3=main()
emp4=main()
print(main.class_variable)
# emp1.print_class_variable()
print('employe number :',main.class_variable)