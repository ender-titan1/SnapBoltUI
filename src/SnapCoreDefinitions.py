from enum import Enum

class Position(Enum):
    NO_POS = 0
    CENTER = 1
    LEFT = 2
    RIGHT = 3
    TOP = 4
    BOTTOM = 5

class Tag:
    def __init__(self, i, indentation, content, context, sd):
        self.indentation = indentation
        self.content = content
        self.context = context
        self.index = i
        self.sd = sd

    def generate_children(self):
        for tag in self.sd.tags: 
            if tag.index < self.index:
                if tag.indentation > self.indentation:
                    self.context.children.append(tag)
                    tag.generate_children()
                else: 
                    break


    def __repr__(self) -> str:
        return f"{self.indentation}: [{self.content} {self.context.size.size1} {self.context.size.size2}] {self.context.pos.pos1} {self.context.pos.off1} {self.context.pos.off2} {self.context.pos.pos2}"

class Context:
    def __init__(self, size, pos, children=[] ):
        self.size = size
        self.pos = pos
        self.children = children

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
