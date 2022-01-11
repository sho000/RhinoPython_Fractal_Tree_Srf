# coding:utf-8
import rhinoscriptsyntax as rs
from Axis import Axis

class Branch(object):
    def __init__(
            self, 
            parentEP, 
            parentLength, 
            parentAxises,
            angleXZ,
            angleXY,
            scale,
            n
            ):
        self.parentEP = parentEP
        self.parentLength = parentLength
        self.parentAxises = parentAxises
        self.angleXZ = angleXZ
        self.angleXY = angleXY
        self.scale = scale
        self.n = n

        self.sP = []
        self.eP = []
        self.length = []
        self.axis = None

        self.setAxis()
        self.setBranch()
    
    def setAxis(self):
        self.axis = Axis(
                    self.parentEP, 
                    self.parentAxises, 
                    self.angleXZ, 
                    self.angleXY
                    ) 
    
    def setBranch(self):
        vec = rs.VectorCrossProduct(self.axis.axises[0], self.axis.axises[1])
        vec = rs.VectorUnitize(vec)
        vec = rs.VectorScale(vec, self.parentLength * self.scale)

        self.sP = self.parentEP
        self.eP = rs.VectorAdd(vec, self.parentEP)

        self.length = rs.Distance(self.sP, self.eP)

    def draw(self):
        guid = rs.AddLine(self.sP, self.eP)
        return guid

    def drawSrf(self):
        pts = []
        # pt0
        if(self.n%2 == 0):
            vec = rs.VectorUnitize(self.axis.axises[0])
        else:
            vec = rs.VectorUnitize(self.axis.axises[1])
        vec = rs.VectorScale(vec, self.length/10/2)
        pt0 = rs.VectorAdd(self.sP, vec)
        pts.append(pt0)
        # pt1
        vec = rs.VectorUnitize(self.axis.axises[2])
        vec = rs.VectorScale(vec, self.length)
        pt1 = rs.VectorAdd(pt0, vec)
        pts.append(pt1)
        # pt2
        if(self.n%2 == 0):
            vec = rs.VectorUnitize(self.axis.axises[0])
        else:
            vec = rs.VectorUnitize(self.axis.axises[1])
        vec = rs.VectorScale(vec, -self.length/10)
        pt2 = rs.VectorAdd(pt1, vec)
        pts.append(pt2)
        # pt3
        vec = rs.VectorUnitize(self.axis.axises[2])
        vec = rs.VectorScale(vec, -self.length)
        pt3 = rs.VectorAdd(pt2, vec)
        pts.append(pt3)
        # srf
        guid = rs.AddSrfPt(pts)
        # return
        return guid

    def drawSrfX(self):
        pts = []
        # pt0
        vec = rs.VectorUnitize(self.axis.axises[0])
        vec = rs.VectorScale(vec, self.length/10/2)
        pt0 = rs.VectorAdd(self.sP, vec)
        pts.append(pt0)
        # pt1
        vec = rs.VectorUnitize(self.axis.axises[2])
        vec = rs.VectorScale(vec, self.length)
        pt1 = rs.VectorAdd(pt0, vec)
        pts.append(pt1)
        # pt2
        vec = rs.VectorUnitize(self.axis.axises[0])
        vec = rs.VectorScale(vec, -self.length/10)
        pt2 = rs.VectorAdd(pt1, vec)
        pts.append(pt2)
        # pt3
        vec = rs.VectorUnitize(self.axis.axises[2])
        vec = rs.VectorScale(vec, -self.length)
        pt3 = rs.VectorAdd(pt2, vec)
        pts.append(pt3)
        # srf
        guid = rs.AddSrfPt(pts)
        # return
        return guid
    
    def drawSrfY(self):
        pts = []
        # pt0
        vec = rs.VectorUnitize(self.axis.axises[1])
        vec = rs.VectorScale(vec, self.length/10/2)
        pt0 = rs.VectorAdd(self.sP, vec)
        pts.append(pt0)
        # pt1
        vec = rs.VectorUnitize(self.axis.axises[2])
        vec = rs.VectorScale(vec, self.length)
        pt1 = rs.VectorAdd(pt0, vec)
        pts.append(pt1)
        # pt2
        vec = rs.VectorUnitize(self.axis.axises[1])
        vec = rs.VectorScale(vec, -self.length/10)
        pt2 = rs.VectorAdd(pt1, vec)
        pts.append(pt2)
        # pt3
        vec = rs.VectorUnitize(self.axis.axises[2])
        vec = rs.VectorScale(vec, -self.length)
        pt3 = rs.VectorAdd(pt2, vec)
        pts.append(pt3)
        # srf
        guid = rs.AddSrfPt(pts)
        # return
        return guid

    def drawText(self):
        text = "n = {}\n".format(self.n)
        text += "angleXZ = {}\n".format(self.angleXZ)
        text += "angleXY = {}".format(self.angleXY)
        pt = rs.VectorAdd(self.sP, self.eP)
        pt = rs.VectorScale(pt,0.5)
        height = 50
        font = None
        font_style = 0
        justification = None
        guid = rs.AddText(text, pt, height, font, font_style, justification)
        color = rs.CreateColor(0,0,0)
        rs.ObjectColor(guid,color)
        # return
        return guid