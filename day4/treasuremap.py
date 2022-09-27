

from operator import pos
from turtle import position


row1 =[" ", " ", " "]
row2 =[" ", " ", " "]
row3 =[" ", " ", " "]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("We do you want to put the treasure: ").split(",")
horiz = int(position[0]) -1 
vert = int(position[1])-1
selected_row = map[vert]
selected_row[horiz] = "X"
print(f"{row1}\n{row2}\n{row3}")
