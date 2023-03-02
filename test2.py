from tkinter import *

print('Hello world!')

arr = [1, 2, 4,6]
print(arr)

Points = [[10,80], [30,40], [80,90]]
print(Points)
print(Points[1])
print(len(Points))

canvas = Canvas(width=100, height=100, bg='white')   # 0,0 is top left corner
canvas.pack(expand=YES, fill=BOTH)                   # increases down, right

PointsLen = len(Points)
pos = 0
for i in Points:
    print(i)
    print(pos)
    print (Points[pos], Points[pos+1])
    canvas.create_line(Points[pos], Points[pos+1])
    pos = pos + 1;
    if pos+1 >= PointsLen:
        break

mainloop()
