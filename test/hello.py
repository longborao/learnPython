
score=20
if score>90:
    print("good")
else:
    print("差")
for i in range(0,2):
    print("item {0}".format(i))
def sayHello():
    print("say hello")
sayHello()
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(11,34))
class hello:
    def __init__(self):
        print("i am hello")
    def __init__(self,name):
        print("hello",name)
    def sayHello(self):
        print()

h=hello("zhangsan")
h.sayHello()
