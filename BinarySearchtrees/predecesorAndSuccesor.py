class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class solution:
    def inpre(self,root):
        self.p = root.left
        while self.p.right:
            self.p = self.p.right
        return self.p

    def insuc(self,root):
        self.p = root.right
        while self.p.left:
            self.p = self.p.left
        return self.p
    def findpresuc(self,root,pre,suc,key):
        if root is None:
            return
        if root.data == key:
            if root.left:
                self.pre = self.inpre(root)

            if root.right:
                self.suc = self.insuc(root)
            return

        if key > root.data:
            







root = node(50)
root.left = node(30)
root.left.left = node(20)
root.left.right = node(40)
root.right = node(70)
root.right.left = node(60)
root.right.right = node(80)
