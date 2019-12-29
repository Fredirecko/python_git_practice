# Diamond Shape Problem - additional overriding practice



class A:
    def methodOne(self):
        print("This method belongs to class A")

class B(A):
    def methodOne(self):
        print("This method belongs to class B")

class C(A):
    def methodOne(self):
        print("This method belongs to class C")

class D(B,C):
    pass

d = D()

d.methodOne()