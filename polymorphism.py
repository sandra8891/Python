class Hi:
    def hiii():
        print("hiiiiii")
class Hello(Hi):
    def hiii():
        print("helloooooo")
obj1=Hello
obj2=Hi
obj1.hiii()
obj2.hiii()