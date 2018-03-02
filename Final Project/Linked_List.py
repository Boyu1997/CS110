class LinkedList:
    def __init__(self, data, child=None):
        self.data = data
        self.child = child

    def getData(self):
        return self.data

    def postData(self, data):
        self.data = data

    def getChild(self):
        return self.child

    def postChild(self, child):
        self.child = child

