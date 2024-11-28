# single inheritance
# class Vehicle:
#     def work():
#         print("move")
# class Car(Vehicle):
#     def wheels():
#         print("four wheels")
# obj1=Car
# obj1.work()

# multilevel inheritance
# class Vehicle:
#     def work():
#         print("move")
# class Car(Vehicle):
#     def wheels():
#         print("four wheels")
# class Swift(Car):
#     def color():
#         print("red")
# obj1=Swift
# obj1.work()
# obj1.wheels()

# multiple inheritance
# class Two_wheeler:
#     def work():
#         print("move")
# class Three_wheeler:
#     def wheels():
#         print("four wheels")
# class Four_wheeler(Two_wheeler,Three_wheeler):
#     def color():
#         print("red")
# obj1=Four_wheeler
# obj1.work()
# obj1.wheels()
# obj1.color()

# hierarchial inheritance
# class Two_wheeler:
#     def work():
#         print("move")
# class Three_wheeler(Two_wheeler):
#     def wheels():
#         print("four wheels")
# class Four_wheeler(Two_wheeler):
#     def color():
#         print("red")
# obj1=Three_wheeler
# obj2=Four_wheeler
# obj1.wheels()
# obj2.color()
# obj1.work()

# Hybrid inheritance
class A1:
    def a11():
        print("a1")
class B1(A1):
    def b11():
        print("b1")
class C1(B1):
    def c11():
        print("c1")
class D1(B1):
    def d11():
        print("d1")
class E1(D1):
    def e11():
        print("e1")
class F1(C1,D1):
    def f11():
        print("f1")
obj1=F1
obj2=E1
obj1.a11()
obj1.b11()
obj1.c11()
obj1.d11()
obj1.f11()
obj2.e11()