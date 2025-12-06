
# Multilevel inheritance

class car:
    def __init__(self,color,name):
        self.name=name
        self.color=color

    def show_color(self):
        print(f'name :',self.name)
        print(f'color :',self.color)

class BMW(car):
    def __init__(self, color,weight):
        car.__init__(self,color,name='bmw')
        self.weight=weight

    def show_color(self):
        car.show_color(self)
        print('weight :',self.weight)
    
class version(BMW):
    def __init__(self, color, version):
        BMW.__init__(self,color,weight='150 kg')
        self.version=version

    def show_color(self):
        BMW.show_color(self)
        print('version :',self.version)

obj=version('White','2.o')
obj.show_color()
