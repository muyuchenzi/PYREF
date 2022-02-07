
# 一种常见的坐标移动问题，经常犯错，很简单的问题都找不到解决办法，这个最简单的问题给自己一个参考
# '''
# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2'''
import math
positon=[0,0]
while True:
    input_string=input()
    if not input_string:
        break
    movement=input_string.split(" ")
    direction=movement[0]
    steps=movement[1]
    if direction=="UP":
        positon[0]+=steps
    elif direction=="DOWN":
        positon[0]-=steps
    elif direction=="LEFT":
        positon[1]-=steps
    elif direction=="RIGHT":
        positon[1]+=steps
    else:
        pass
result=int(round(math.sqrt(positon[0]**2+positon[1]**2)))