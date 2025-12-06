
# Hybrid Inheritance

class A:
    def __init__(self,name):
        self.name=name
    def sh(self):
       print('class A')

class B(A):
    def sho(self):
        print('class B')

class C(A):
    def show(self):
        print('class C',self.name)

class D(B,C):
    def show(self):
        print('class D')


ob_A=A('Arbaj')
# ob_C=C('Ayan')
ob_D=D('sahil')
ob_A.sh()
# ob_C.sh()
ob_D.sho()