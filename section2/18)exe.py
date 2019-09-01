#person = [mujju,salman,thuss]
def who_do_you_know():
    answer = input("Enter the name of people you know, seperated by commas")
    people_list = people.split(",")
    return people_list

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("you know {}!".format(person))

print(ask_user())

