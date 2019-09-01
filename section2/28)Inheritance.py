class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks/ len(self.marks))

    def friend(self, friend_name):
        return student(friend_name, self.school)

class Workingstudent(student):
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.salary = salary
        self.marks = []

anna = Workingstudent("Anna", "Oxford", 40000)
print(anna.salary)

friend = Workingstudent.friend("Mujju", 50000)

print(friend.name)
print(friend.school)
print(friend.salary)