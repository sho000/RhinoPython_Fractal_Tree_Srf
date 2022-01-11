# coding:utf-8
from Tree import Tree
import rhinoscriptsyntax as rs
import random

random.seed(0)

# instance of Tree
trees = []
xNum = 2
yNum = 2
for y in range(yNum):
    for x in range(xNum):
        tree = Tree()
        trees.append(tree)

# draw branch
rs.EnableRedraw(False)
xPitch = 15000
yPitch = 15000
for y in range(yNum):
    for x in range(xNum):
        index = y*xNum + x
        for branch in trees[index].branches: 
            # movePt
            movePt = [x*xPitch,y*yPitch,0]
            # axis
            guid = branch.axis.draw()
            rs.MoveObject(guid,movePt)
            # draw
            guid = branch.draw()
            rs.MoveObject(guid,movePt)
            # 
            if(branch.n%2 == 0):
                # drawSrfX
                guid = branch.drawSrfX()
                rs.MoveObject(guid,movePt)
                color = rs.CreateColor(255,0,0)
                rs.ObjectColor(guid, color)
                # drawSrfY
                guid = branch.drawSrfY()
                rs.MoveObject(guid,movePt)
                color = rs.CreateColor(0,255,0)
                rs.ObjectColor(guid, color)
            else:
                # drawSrfX
                guid = branch.drawSrfX()
                rs.MoveObject(guid,movePt)
                color = rs.CreateColor(0,255,0)
                rs.ObjectColor(guid, color)
                # drawSrfY
                guid = branch.drawSrfY()
                rs.MoveObject(guid,movePt)
                color = rs.CreateColor(255,0,0)
                rs.ObjectColor(guid, color)
            # drawText
            guid = branch.drawText()
            rs.MoveObject(guid,movePt)
rs.EnableRedraw(True)