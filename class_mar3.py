Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
class Student:
    def display(self):
        print("Welcome to class Prog")

        
obj = Student()
obj.display()
Welcome to class Prog
class Student:
     def display(self):
           print("Welcome to class Prog")
     def details(self):
         print("Something....")

         
        
obj = Student()
odj.details()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    odj.details()
NameError: name 'odj' is not defined. Did you mean: 'obj'?
obj.details()
Something....
obj.display()
Welcome to class Prog
class Student:
    def inputData(self, name, roll):
        self.name=name
        self.roll=roll
    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)

        
s1=Student()
s1.inputData("Shravya",01)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
s1.inputData("Shravya",1)
s1.display()
Name: Shravya
Roll: 1
s1.name="Gayathri"
s1.roll=2
s1.display()
Name: Gayathri
Roll: 2
class Student:
    Name="Gangamma"
    Age=18
    def inputData(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print ("Name:", self.name)
        print ("Age:", self.age)

        
s1=Student
s1=Student()
s1.inputData("Gangamma", 18)
s1.display
<bound method Student.display of <__main__.Student object at 0x000001ADEA0D17F0>>
s1.display()
Name: Gangamma
Age: 18
class Student:
    name="Gangamma"
    age=18
    def inputData(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print ("Name:", self.name)
        print ("Age:", self.age)

        
s1=Student()
s1.display()
Name: Gangamma
Age: 18
n = input("Entner a name:")
Entner a name:Shravya
a=int(input("entetr the age:"))
entetr the age:18
s1.inputData(n,a)
s1.display()
Name: Shravya
Age: 18

#write this code in module and execute

=================================================== RESTART: C:/Users/HP/Desktop/PYTHON/student_modules_mar3.py ===================================================
Shravya
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    Shravya
NameError: name 'Shravya' is not defined

========================================================= RESTART: C:/Users/HP/Desktop/PYTHON/main_mar3.py ========================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/PYTHON/main_mar3.py", line 1, in <module>
    from student_module import Student
ModuleNotFoundError: No module named 'student_module'

========================================================= RESTART: C:/Users/HP/Desktop/PYTHON/main_mar3.py ========================================================
Traceback (most recent call last):
  File "C:/Users/HP/Desktop/PYTHON/main_mar3.py", line 1, in <module>
    from student_module_mar3 import Student
ModuleNotFoundError: No module named 'student_module_mar3'

========================================================= RESTART: C:/Users/HP/Desktop/PYTHON/main_mar3.py ========================================================
Enter a name: Shravya
Enter age: 18
Name: Shravya
Age: 18



#rename the variable self to s

========================================================= RESTART: C:/Users/HP/Desktop/PYTHON/main_mar3.py ========================================================
Enter a name: Gangamma
Enter age: 18
Name: Gangamma
Age: 18


class Employee:
    def_init_(self, name, age):
        
SyntaxError: invalid syntax
class Employee:
    def _init_(self, name, age):
        self.name=name
        self.age=age
    def diplay(self):
        print("Nmae:",self.name)
        print("Age:", self.age)

        
e1=Employee()
e1._init_("Shravya",18)
e1.display()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    e1.display()
AttributeError: 'Employee' object has no attribute 'display'. Did you mean: 'diplay'?
e1.diplay
<bound method Employee.diplay of <__main__.Employee object at 0x000002305CF0D940>>
e1.diplay()
Nmae: Shravya
Age: 18
e2=Employee
e2.diplay()
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    e2.diplay()
TypeError: Employee.diplay() missing 1 required positional argument: 'self'
class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def diplay(self):
        print("Nmae:",self.name)
        print("Age:", self.age)
e1=Employee()
SyntaxError: invalid syntax
e1=Employee("Shravya",18)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    e1=Employee("Shravya",18)
TypeError: Employee() takes no arguments
e1=Employee("Shravya",18)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    e1=Employee("Shravya",18)
TypeError: Employee() takes no arguments
class Employee:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def diplay(self):
        print("Nmae:",self.name)
        print("Age:", self.age)

        
e1=Employee("Shrravya",18)
e1.diplay()
Nmae: Shrravya
Age: 18

class Student:
    def __init__(self, name):
        self.name=name
    def name(self, name):
        self.name=name
    def display(self)
    
SyntaxError: expected ':'
class Student:
    def __init__(self, name):
        self.name=name
    def name(self, name):
        self.name=name
    def display(self):
        print("Nmae:", self.name)

        
s=Student("Shravya",18)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    s=Student("Shravya",18)
TypeError: Student.__init__() takes 2 positional arguments but 3 were given
s=Student("Shravya")
s.display()
Nmae: Shravya
s.name("Gayathri")
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    s.name("Gayathri")
TypeError: 'str' object is not callable
s=student("Om")
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    s=student("Om")
NameError: name 'student' is not defined. Did you mean: 'Student'?
s=Student("OM"
          0
          
SyntaxError: '(' was never closed
s=Student("OM)
          
SyntaxError: unterminated string literal (detected at line 1)
>>> s=Student("OM")
...           
>>> s.display
...           
<bound method Student.display of <__main__.Student object at 0x000002305CE43610>>
>>> s.display()
...           
Nmae: OM
>>> 
>>> class Student:
...     def __init__(self, name):
...         self.name=name
...     def name(self, name):
...         self.name=name
...     def display(self):
...         print("Nmae:", self.name)
...         print("Name Data", self.n)
... 
...         
>>> s=Student("OM")
>>> s.inputName("Shravya")
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    s.inputName("Shravya")
AttributeError: 'Student' object has no attribute 'inputName'
>>> class Student:
...     def __init__(self, name):
...         self.name=name
...     def inputName(self, n):
...         self.n=n
...     def display(self):
...         print("Nmae:", self.name)
...         print("Name Data", self.n)
... 
...         
>>> s=Student("OM")
>>> s.inputName("Shravya")
>>> s.display()
Nmae: OM
Name Data Shravya
