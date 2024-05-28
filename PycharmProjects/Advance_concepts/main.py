# import pettytable
# from turtle import Turtle,Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.color("yellow")
# timmy.shape("square")
# my_screen = Screen()
# print(my_screen.exitonclick())
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squritle","Cahrmander"])
table.add_column("Type",["Electric","Water","fire"])
print(table)