from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
while(1>0):
    timmy.shape("turtle")
    timmy.color("Blue")
    timmy.forward(100)
    timmy.left(100)
    timmy.forward(100)
    timmy.right(25)
    timmy.forward(100)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",[ "Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"

print(table)

