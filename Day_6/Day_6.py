'''Functions & While Loops '''

# Creating a new functions 

# def my_function():
#     #Do this
#     #Then do this
#     #Finally do this

# def my_function():
#     print("Hello")
#     print("By")

# my_function()


# Exercise on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def move_robot():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# move_robot()
# move_robot()
# move_robot()
# move_robot()
# move_robot()
# move_robot()

#While Loops

# while something_is_true:
    #Do this
    #Then do this
    #Finally do this

# Exercise on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def move_robot():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# while  not at_goal():
#     move_robot()


# Exercise on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def move_robot():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         move_robot()
#     else:
#         move()

# Exercise on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def move_robot():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         move_robot()
#     else:
#         move()

# Final project - The Maze https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json



# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if right_is_clear == True and front_is_clear == True:
#         turn_right()
#     elif wall_in_front() == True and wall_on_right() == True:
#         turn_left()
#     elif wall_in_front() == True and wall_on_right() == False:
#         turn_right()
#     else:
#         move()
