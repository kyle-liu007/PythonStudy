class stu(object):
    name = None
    age = 18
    def fun(self):
        print("hhh")
        return None
a = stu()
print(a.name)
a.fun()
print(stu.__dict__)
print(a.__dict__)
