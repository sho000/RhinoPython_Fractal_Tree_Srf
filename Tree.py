
# coding:utf-8
from Branch import Branch
import rhinoscriptsyntax as rs
import random
import scriptcontext

class Tree(object):
    def __init__(self):
        self.branches = []
        self.minScale = 0.8
        self.maxScale = 0.95
        self.minXZAngle = 10
        self.maxXZAngle = 35
        self.minXYAngle = 60
        self.maxXYAngle = 90

        # parent
        parentEP = [0,0,0]
        parentLength = 2000
        parentAxises = [
            [300,0,0],
            [0,300,0],
            [0,0,300]
        ]

        angleXZ = 0
        angleXY = 0
        scale = 1
        n = 0

        # child
        branch = Branch(
            parentEP, 
            parentLength, 
            parentAxises,
            angleXZ,
            angleXY,
            scale,
            n
        )
        self.branches.append(branch)

        # recursion
        self.makeChildBranch(branch,n+1)

    def makeChildBranch(self,branch,n):
        # end condition
        if(n>6):
            return

        # left branch
        parentEP = branch.eP
        parentLength = branch.length
        parentAxises = branch.axis.axises
        angleXZ = random.uniform(self.minXZAngle, self.maxXZAngle)
        # angleXY = random.uniform(self.minXYAngle, self.maxXYAngle)
        angleXY = 90
        scale = random.uniform(self.minScale, self.maxScale)
        leftBranch = Branch(
            parentEP, 
            parentLength, 
            parentAxises,
            angleXZ,
            angleXY,
            scale,
            n
        )
        self.branches.append(leftBranch)
        self.makeChildBranch(leftBranch, n+1)

        # right branch
        parentEP = branch.eP
        parentLength = branch.length
        parentAxises = branch.axis.axises
        angleXZ = random.uniform(self.minXZAngle, self.maxXZAngle)
        # angleXY = -random.uniform(self.minXYAngle, self.maxXYAngle)
        angleXY = -90
        scale = random.uniform(self.minScale, self.maxScale)
        rightbranch = Branch(
            parentEP, 
            parentLength, 
            parentAxises,
            angleXZ,
            angleXY,
            scale,
            n
        )
        self.branches.append(rightbranch)
        self.makeChildBranch(rightbranch, n+1)