class TreeNode:
    def __init__(self,data,children=[])->any:
        self.data = data
        self.children = children

    def __str__(self,level=0)-> any:
        ret = "   " * level+str(self.data) +"\n"
        for child in self.children:
            ret = ret + child.__str__(level + 1)
        return ret
    
    def addChild(self,TreeNode)-> any:
        self.children.append(TreeNode)

tree = TreeNode("Drinks",[])
cold = TreeNode("cold",[])
hot = TreeNode("hot",[])

tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode("Tea",[])
coffee = TreeNode("Coffee",[])

beer = TreeNode("Beer",[])
limca = TreeNode("Limca",[])

cold.addChild(beer)
cold.addChild(limca)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)

