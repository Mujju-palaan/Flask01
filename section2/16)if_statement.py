friends = ["mujju","salman","thuss","mariyam"]

answer = input("Enter the friend you know: ")

if answer in friends:
    print("you know my friends")
    print("you know {} !".format(answer)    + "great")

else:
    print("get the hell out of here!.....you Stranger")
    print("get the hell out of here!  {}".format(answer) +   "is not my friend")