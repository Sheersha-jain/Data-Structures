class Test:
    """test class"""
    i = 23
    def func(self):
        j=0
        print("hello")

Test.func(Test)

x =Test()

print(Test())
print(x)
print(Test)
print(Test())

class Practice:
    """practice class"""
    hello ='hey'

    def func(self):
        print("hey hi")

print(Practice.__doc__)

print(Practice.hello)
print(Practice)
Practice.func(Practice)
print(type(Practice.func(Practice)))
print("value",Practice.func(Practice))
print("here"), Practice.func(Practice)
print(Practice.func)
ob = Practice()
print(ob.func)