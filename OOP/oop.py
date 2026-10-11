class college:
    def __init__(self,name,roll,id):
        self.name = name
        self.roll = roll
        self.id = id

std = college("khan","233","ai")
print(std.name,std.id,std.roll)

#---------------------------------------------------------------------------------------------------

class student:
    def __init__ (self,name,id):
        self.name = name
        self.id = id
std_name = input("enter student name: ")
std_id = input("enter student id : ")
std = student(std_name,std_id)
print(f"student name is {std_name} and his id is {std_id}")

#---------------------------------------------------------------------------------------------------

# initialization of the class employee
class employee:
    def __init__(self):
        self.id = 1
        self.salary = 50000
        self.designation = "SDE"

# when creating a function in class it is called method
    def travel (self,destination):
        print(f"the employee is traveling toward {destination}")
# creating an object or an instance of the class employee
sam = employee()

#printing an attribute
print(f"i am sam and my id is {sam.id}\n my salary is {sam.salary} \n and my designation is {sam.designation}")
# calling a method
sam.travel("UAE")
