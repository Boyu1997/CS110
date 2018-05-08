class Tree:

    def __init__(self, key, parent, landing="NA"):
        self.key = key
        self.successor = []
        self.parent = parent
        self.children = dict()
        self.landing = landing

    def add_chile(self, name, counter=0):

        if name[counter] in self.children:
            if counter is len(name)-1:
                self.children[name[counter]].successor.append(name)
            else:
                self.children[name[counter]].add_chile(name, counter+1)

        else:
            self.children[name[counter]] = Tree(name[counter], self)
            self.add_chile(name, counter)



def find_landing(root):
    for node in root.children():
        if node.landing is "NA":
            while True:
                return # add here
        find_landing(node)










string = "The pot had a handle."


set = ["The", "han", "and", "pork", "port", "pot", "ha", "e"]

root = Tree("root", "NA", "root")
for entry in set:
    root.add_chile(entry)





