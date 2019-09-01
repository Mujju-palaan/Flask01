my_variable = "holla"
for i in my_variable:
    print(i)

my_list = [1,2,3,4,5]
for num in my_list:
    print(num**2)

user_num = True
while user_num == True:
    print(10)
    answer = input("Should we print it again? (y/n)")
    if answer == 'n' :
        user_num = False
