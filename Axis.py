#coding:utf-8
import rhinoscriptsyntax as rs

class Axis(object):
    def __init__(
            self, 
            parentEP, 
            parentAxises, 
            angleXZ, 
            angleXY
            ):
        self.parentEP = parentEP
        self.parentAxises = parentAxises
        self.angleXZ = angleXZ
        self.angleXY = angleXY

        self.axises = []
        self.setAxis()
    
    def setAxis(self):
        # XZ
        newAxises1 = []
        for axis in self.parentAxises:
            newAxis = rs.VectorRotate(axis, self.angleXZ, self.parentAxises[1])
            newAxises1.append(newAxis)
        # XY
        newAxises2 = []
        for axis in newAxises1:
            newAxis = rs.VectorRotate(axis, self.angleXY, self.parentAxises[2])
            newAxises2.append(newAxis)

        self.axises = newAxises2

    def draw(self):
        guids = [] 
        # x
        x = rs.VectorAdd(self.parentEP,self.axises[0])
        guid = rs.AddLine(self.parentEP, x)
        color = rs.CreateColor(255,0,0)
        rs.ObjectColor(guid,color)
        guids.append(guid)

        # y
        y = rs.VectorAdd(self.parentEP,self.axises[1])
        guid = rs.AddLine(self.parentEP, y)
        color = rs.CreateColor(0,255,0)
        rs.ObjectColor(guid,color)
        guids.append(guid)

        # z
        z = rs.VectorAdd(self.parentEP,self.axises[2])
        guid = rs.AddLine(self.parentEP, z)
        color = rs.CreateColor(0,0,255)
        rs.ObjectColor(guid,color)
        guids.append(guid)

        return guids