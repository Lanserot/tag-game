class Storage:

    def __init__(self):
        self.menuClass = None
        self.rendererClass = None
        self.memoryClass = None
        self.fieldClass = None
        self.logicClass = None

    def getMemoryClass(self):
        return self.memoryClass

    def getRendererClass(self):
        return self.rendererClass

    def getMenuClass(self):
        return self.menuClass

    def getFieldClass(self):
        return self.fieldClass

    def getLogicClass(self):
        return self.logicClass