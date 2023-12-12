# from turtle import Turtle, Screen
# # Initializing/Create an object
# timmy = Turtle()
# print(timmy)
# # Calling methods to change turtles attributes
# timmy.shape("turtle")
# timmy.color("purple")
# # Make the turtle move
# timmy.forward(100)
# # Accessing attributes from an object by the . notation
# my_screen = Screen()
# print(my_screen.canvheight)
# # Calling a method/function from an object
# my_screen.exitonclick()

from prettytable import PrettyTable, FRAME

# Initialize Object
table = PrettyTable()
# Create columns with their respective field labels and column data
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# Change table alignment to left align
table.align = "l"
print(table)