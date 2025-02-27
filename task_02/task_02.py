import turtle
import math


def pythagoras_tree(branch_length, level):
    if level == 0:
        return

    turtle.forward(branch_length)
    turtle.left(45)
    pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)
    turtle.right(90)
    pythagoras_tree(branch_length * math.sqrt(2) / 2, level - 1)
    turtle.left(45)
    turtle.backward(branch_length)


def main():
    level = int(input("Введіть рівень рекурсії від 5 до 10: "))
    level = min(level, 10)

    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -200)
    turtle.down()

    pythagoras_tree(100, level)

    turtle.done()


if __name__ == "__main__":
    main()
