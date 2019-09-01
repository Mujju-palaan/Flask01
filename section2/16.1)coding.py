numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def evens_num(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0 :
            evens.append(num)
    return evens
print(evens_num(numbers))

def user_menu(choice):
    if choice == 'a':
        return "Add"
    if choice == "q" :
        return "Quit"
print(user_menu(choice))