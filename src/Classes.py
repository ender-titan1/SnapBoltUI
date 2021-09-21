
class Tag:
    def __init__(self, indentation, content, context):
        self.indentation = indentation
        self.content = content
        self.context = context

class Context:
    def __init__(self, size, pos ):
        self.size = size
        self.pos = pos
class Pos:
    def __init__(self, pos1, off1, pos2, off2):
        self.pos1 = pos1
        self.pos2 = pos2
        self.off1 = off1
        self.off2 = off2

class Size:
    def __init__(self, size1, size2):
        self.size1 = size1
        self.size2 = size2
