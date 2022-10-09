import random as r
import turtle as t

t.speed(1000)
color = ['red', 'green', 'blue']

input_number = int(input("몇 번 돌릴래 : "))


for x in range(input_number):
    t.color = r.choice(color)
    t.circle(10)
    t.left(1)
