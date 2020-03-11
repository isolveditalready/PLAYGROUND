#1.how have you used python in the past?


#2.fibonacci 

 a, b = 0,1
 for i in xrange(0,1):
	print a
	a,b = b, a+b




#lists
my_list = [10,20,30,40,50]
# for i in my_list:
# 	print i

#tuples
my_tup = (1,2,3,4,5,6,7,8)
# for i in my_tup:
# 	print i

#Dict
my_dict = {'name':'Bronx','age':'2','occupation':"owner's dog"}
# for key,val in my_dict.iteritems():
#	print(f"my {key} is {val})


#set
my_set = {10,20,30,40,50}
# for i in my_set:
#	print i



#3.list comprehensions

my_list [ 1,2,3,4]

squares = [num*num for num in my_list]
print squares


#4.generators. ## fibnacci

def fib(num):
	a,b = 0,1
	for i in xrange(0,num):
		yield f"{i+1},{a}"
		a,b = b, a+b

for item in fib(10):
	print item



#.basic OOP

class Person(object):
	def __init__(self,name):
		self.name = name
	def reveal_identity(self):
		print(f"My name is {self.name}")

class SuperHero(Person):
	def __init__(self,name,hero_name):
		super(SuperHero, self).__init__(name)
		self.hero_name = hero_name

	def reveal_identity(self):
		super(SuperHero,self).veal_identity()
		print(f".. and I am {self.hero_name}")


# lambda function :  anonymous function
a = lambda x,y: x+y
print(a(5,6))

## do you understand [:]
# a = [1,2,3,4,5]
#____________________________________
# a[:] >>> [1, 2, 3, 4, 5]
# a[:2] >>> [1, 2]
# a[2:] >>> [3, 4, 5]
# a[::-1]>>> [5, 4, 3, 2, 1]
# a[1:3] >>> [2, 3]


# decorator
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        rv = func()
        total = time.time() - start
        print("time : " , total)
        return rv
    return wrapper

#decorator declaration 
@timer
def test():
    for _ in range(1000000):
        pass
@timer
def test2():
    time.sleep(2)

test()
test2()