# import
import rhinoscriptsyntax as rs
import random as rnd

#******************************
# Branch class
#******************************
class Branch():
    def __init__(self,sP,eP):
        self.sP = sP
        self.eP = eP
        
    def drawBranch(self):
        id = rs.AddLine(self.sP, self.eP)
        return id

#******************************
# Tree class
#******************************
class Tree():
    def __init__(self):
        # first branch
        sP = [0,0,0]
        eP = [0,1800,0]
        self.branches = []
        branch = Branch(sP,eP)
        self.branches.append(branch)
        self.makeChildBranch(branch,0)
        
    def makeChildBranch(self,branch,n):
        # exit conditions
        if(n==5):
            return
            
        # parent branch
        vec = rs.VectorSubtract(branch.eP, branch.sP)
        vecU = rs.VectorUnitize(vec)
        
        # left branch
        angle = rnd.randint(10,45)
        length = rs.Distance(branch.sP,branch.eP)*rnd.uniform(0.8,0.9)
        newEP = rs.VectorRotate(vecU,angle,[0,0,1])
        newEP = rs.VectorScale(newEP,length)
        newEP =  rs.VectorAdd(branch.eP,newEP)
        newSP = branch.eP
        leftBranch = Branch(newSP,newEP)
        self.branches.append(leftBranch)
        self.makeChildBranch(leftBranch,n+1)
        
        # right branch
        angle = -rnd.randint(10,45)
        length = rs.Distance(branch.sP,branch.eP)*rnd.uniform(0.8,0.9)
        newEP = rs.VectorRotate(vecU,angle,[0,0,1])
        newEP = rs.VectorScale(newEP,length)
        newEP =  rs.VectorAdd(branch.eP,newEP)
        newSP = branch.eP
        rightBranch = Branch(newSP,newEP)
        self.branches.append(rightBranch)
        self.makeChildBranch(rightBranch,n+1)
        
    def drawTree(self,movePt):
        for branch in self.branches:
            id = branch.drawBranch()
            rs.MoveObject(id,movePt)


#**********************
# main
#**********************
if(__name__ == "__main__"):
    # inctances
    trees = []
    for y in range(5):
        for x in range(5):
            tree = Tree()
            trees.append(tree)
    
    # draw
    rs.EnableRedraw(False)
    cnt = 0
    for y in range(5):
        for x in range(5):
            movePt = [x*10000,y*10000,0]
            trees[cnt].drawTree(movePt)
            cnt+=1
    rs.EnableRedraw(True)