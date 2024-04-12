# print('hello {1} {0:.4s} {2:s} '.format('this second', 'first', 'and last'))
# t=(1,2,3,"ll",True,5.3)
# print(t[0])
# t2=9,3,7,9
# t3=t+t2
# print(t3)
# x={11,9,3,4,9,3,2,8,2.2,'o',"ll",True}
# print(x)
# y={5,6,3,7,1,2}
# print(x.symmetric_difference(y))
# z=set(t3)
# print(z)
# S=input('JHGF')

# x=10
# if x==5:
#     print('bad')
# elif x==7:
#     print('not')
# else:
#     print('good')

# isValid=0
# print("this is valid" if isValid else "this is not valid")

# x=1
# while x<=10:
#     print('islam')
#     x+=1

# for i in range(1,6):
#     print('hasib')

# myRange = range(1, 101)
# mySkills = {
# "Html": "90%",
# "Css": "60%",
# "PHP": "70%",
# "JS": "80%",
# "Python": "90%",
# "MySQL": "60%"
# }
# for skill in mySkills:
#     if skill == 'PHP':
#         continue
#     else:
#         print(f"My Progress in Lang {skill} \Is:{mySkills[skill]}")


# myDict = {
# 'one': 1,
# 'two':2,
# 'three':3,
# 'four':4
# }
# for key in myDict:
#     print(key, myDict[key])


# def addition(*Ns):
#     # result = 0
#     # for n in Ns:
#     #     result += n
#     # return result
#     return Ns

# print(addition(23, 456, 8, 94, 89, 34, 79, 32))


# x = 1

# def one():
#     global x
#     x = 2
#     print(f"Print Variable From Function Scope {x}")

# def two():
#     x = 10
#     print(f"Print Variable From Function Scope {x}")
#     one()
#     print(f"Print Variable From Global Scope {x}")
#     print(f"Print Variable From Global Scope After One Function Is Called {x}")

# one()
# two()


# def divide_numbers(a, b):
# 	"""
# 	Divide two numbers.

# 	Parameters
# 	----------
# 	a : float
# 		The dividend.
# 	b : float
# 		The divisor.

# 	Returns
# 	-------
# 	float
# 		The quotient of the division.
# 	"""
# 	if b == 0:
# 		raise ValueError("Division by zero is not allowed.")
# 	return a / b
# print(divide_numbers(3,0))


# class test:
#     x=10
#     @classmethod
#     def users(cls):
#         print(f"class method test{cls.x}")
#     @staticmethod
#     def prof():
#         print("hello user")

# test.users()
# print(test.x)
# test.prof()


# class Food:
#     @classmethod
#     def potato(cls):
#         print("potato in class")
#     x=10
#     def __init__(self, name):
#         self.name=name
#         print(f"{self.name} is Created From Base Class")
#     def eat(self,test):
#         print(f"{test} Eat Method From Base Class")

# class Apple(Food):
#     def __init__(self, name, last):
#         self.last=last
#         super().__init__(name)
#         print(f"{self.name} {self.last} Apple is Created From Derived Class")
#         print(Apple.x+15)

# food_one=Food('islam')
# food_two=Apple()
# food_two.eat('meet')
# food_two.potato()
# Apple.potato()
# print(food_two.x)
# print(Apple.x)

# food_one=Food('islam')
# food_two=Apple('islam', 'hasib')




# class Parent1:
#     def __init__(self, value1):
#         self.value1 = value1

#     def method1(self):
#         print("Method from Parent1")

# class Parent2:
#     def __init__(self, value2):
#         self.value2 = value2

#     def method2(self):
#         print("Method from Parent2")

# class Child(Parent1, Parent2):
#     def __init__(self, value1, value2, child_value):
#         # Call the __init__ methods of both parent classes using super()
#         super().__init__(value1)
#         super(Parent2, self).__init__(value2)  # Specify the parent class for multiple inheritance
#         self.child_value = child_value

#     def child_method(self):
#         print("Method from Child")

# # Creating an instance of the Child class
# child_obj = Child("Value1", "Value2", "ChildValue")

# # Accessing attributes from both parent classes
# print(child_obj.value1)  # Output: Value1
# print(child_obj.value2)  # Output: Value2

# # Calling methods from both parent classes
# child_obj.method1()  # Output: Method from Parent1
# child_obj.method2()  # Output: Method from Parent2

# # Calling the child method
# child_obj.child_method()  # Output: Method from Child

## #overload
# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# # Creating an instance
# calculator = Calculator()
# # Using the overloaded method
# result1 = calculator.add(1)
# result2 = calculator.add(1, 2)
# result3 = calculator.add(1, 2, 3)
# print(result1)  # Output: 1
# print(result2)  # Output: 3
# print(result3)  # Output: 6

## #polymorphsim ==>override
# class a:
#     def do_it(self):
#         print("do from a")
#         raise NotImplementedError("must be implement from each inhert class")

# class b(a):
#     def do_it(self):
#         print("do from b")

# bb=a()
# bb.do_it()

# ##abstract
# from abc import ABCMeta, abstractmethod
# class programming(metaclass=ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass

# class python(programming):
#     def has_oop(self):
#         return "yes"

# class pascal(programming):
#     def has_oop(self):
#         return "no"

# p=pascal()
# print(p.has_oop())

import os

# print(os.getcwd())
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# os.chdir(os.path.dirname(os.path.abspath(__file__)))

# file = open(r'filetest.txt','r')
# print(file.name)
# print(file.mode)
# print(file.encoding)

# print(file.read())
# print(file.readline())
# print(file.readline())

# print(file.readlines())

# file.close()

# file=open('filetest.txt','w')
# file.write("Hello from python file with love")
# file.write("islam hasib\n"*1000)

# list=['islam\n', 'hasib\n', 'thabet\n', 'aly\n']
# file.writelines(list)


# file=open('filetest.txt','a')
# file.write("Hello from python file with love\n")
# file.write("islam hasib\n")

# file=open('filetest.txt','a')
# file.truncate(25)
# print(file.tell())


# file=open('test2','x')



# ''' JavaScript Object Notation '''
# import json

# with open('states.json') as f:
#    data = json.load(f)
# for state in data['states']:
#    del state['area_codes']

# with open('new_states.json', 'w') as f:
#    json.dump(data, f, indent=2)


# import json
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()
# print(source)
# data = json.loads(source)

# # print(json.dumps(data, indent=2))

# usd_rates = dict()

# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price

# print(50 * float(usd_rates['USD/INR']))


# import datetime
# print(datetime.datetime(1999, 2, 15, ))


# import unittest
# class tests(unittest.TestCase):
#     def test1(self):
#         self.assertEqual(10 + 110, 20, "should be = 30")
#         self.assertRaises(ValueError,)

# if __name__=="__main__":
#     unittest.main()


# import os
# from cmd import Cmd

# class MyPrompt(Cmd):

#     _AVAILABLE_COLORS = ('blue', 'green', 'yellow', 'red', 'black')

#     def do_hello(self, args):
#         """Says hello. If you provide a name, it will greet you with it."""
#         if len(args) == 0:
#             name = 'stranger'
#         else:
#             name = args
#         print ("Hello, %s" % name)

#     def do_quit(self, args):
#         """Quits the program."""
#         print ("Quitting.")
#         raise SystemExit
    
#     def do_add(self,s):
#         l = s.split()
#         if len(l)!=2:
#             print ("*** invalid number of arguments")
#             return
#         try:
#             l = [int(i) for i in l]
#         except ValueError:
#             print ("*** arguments should be numbers")
#             return
#         print (l[0]+l[1])

#     def help_add(self):
#         print ('add two integral numbers')

#     def help_introduction(self):
#         print ('introduction')
#         print ('a good place for a tutorial')
    
#     def emptyline(self):
#         pass

#     def preloop(self):
#         print ('Hello')
#     def postloop(self):
#         print ('Goodbye')

#     def do_shell(self, s):
#         os.system(s)
#     def help_shell(self):
#         print ("execute shell commands")

# if __name__ == '__main__':
#     prompt = MyPrompt()
#     prompt.prompt = '>>> '
#     prompt.cmdloop('Starting prompt...')


# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print("The value of {} is {}".format(key, value))

# print_values(
#             name_1="Alex",
#             name_2="Gray",
#             name_3="Harper",
#             name_4="Phoenix",
#             name_5="Remy",
#             name_6="Val"
#         )


# def some_args(arg_1, arg_2, arg_3):
#     print("arg_1:", arg_1)
#     print("arg_2:", arg_2)
#     print("arg_3:", arg_3)

# args = ("Sammy", "Casey", "Alex")
# some_args(*args)


# def some_args(arg_1, arg_2, arg_3):
#     print("arg_1:", arg_1)
#     print("arg_2:", arg_2)
#     print("arg_3:", arg_3)

# my_list = [2, 3]
# some_args(1, *my_list)


# def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
#     print("kwarg_1:", [kwarg_1])
#     print("kwarg_2:", kwarg_2)
#     print("kwarg_3:", kwarg_3)

# kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
# some_kwargs(**kwargs)


def my_fct(*args, **kwargs):
    print("{} - {}".format(args, kwargs))

my_fct() # () - {}
my_fct("Best") # ('Best',) - {}
my_fct("Best", 89) # ('Best', 89) - {}
my_fct(name="Best") # () - {'name': 'Best'}
my_fct(name="Best", number=89) # () - {'name': 'Best', 'number': 89}
my_fct("School", 12, name="Best", number=89) # ('School', 12) - {'name': 'Best', 'number': 89}
