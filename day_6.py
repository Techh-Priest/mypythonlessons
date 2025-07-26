        ## Functions, Code Blocks, Indentation and While Loops
    #1. Functions.
#Python has a lot of built-in functions for example: The print() function, int() fuction, input() function, len() function etc.
#Now what do we do when we want to create our own fucntions?
# Well, we start by defining a fucntion using def:
def my_function():
    print("Hello")
    print("Bye") #First create/define and name the function then specify what it should do.
my_function() #Then call it to run/execute/use the function by calling the name of the function.

        #Let's look at Reeborg's World on Chrome
#Functions help store long line of code/instruction for repeated/future use


    #While Loop

#This loop looks something like this:
# while something_is_true
    #Do this repeatedly

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# def hurdle_jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# #for hurdle in range(0, 6):
# #    hurdle_jump()
#
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     hurdle_jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)


#When to use a For Loop and a While Loop:
        # For Loop is perfect when you are iterating over something and
        # you want to do something with each thing you iterate over

        # A While Loop is perfect when you want to carry out some
        # functionality as many times as possible until a certain condition you've set is met.

        # While Loop are a little dangerous because it will keep running until a condition is met and it
        # evolves into an Infinite Loop.

            ## Hurdle 4 Challenge
        # def turn_right():
        #     turn_left()
        #     turn_left()
        #     turn_left()
        #
        #
        # def hurdle_jump():
        #     turn_left()
        #     while wall_on_right():
        #         move()
        #     turn_right()
        #     move()
        #     turn_right()
        #     while front_is_clear():
        #         move()
        #     turn_left()
        #
        #
        # while at_goal() == False:
        #     if wall_in_front():
        #         hurdle_jump()
        #     else:
        #         move()


        ### Maze Challenge: Intermediate Level Code Solution. Come Back Here Later After Day 15:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# while at_goal() == False:
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()