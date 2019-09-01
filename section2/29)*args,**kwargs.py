def my_list_addition(list_arg):
    return sum(list_arg)
noob = my_list_addition([3,4,56,7,8,9,8,8])
print(noob)

def addition_simplified(*args):
    return sum(args)
thuss = addition_simplified(3,4,56,7,8,9,8,8)
print(thuss)

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwargs(12,23,34, name='Mujju', location='Wgl')

#################################3


class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/ len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)
####
class Workingstudent(student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = Workingstudent("Anna", "Oxford", 40000)
print(anna.salary)

friend = Workingstudent.friend(anna, "Mujju", 50000)

print(friend.name)
print(friend.school)
print(friend.salary)
