import string
from enum import Enum

INDENTATION_INTERVAL = 4

class PositionType(Enum):
    CENTER = 1
    LEFT = 2
    RIGHT = 3
    TOP = 4
    BOTTOM = 5
    SNAP_UNDER = 6
    SNAP_OVER = 7
    NO_POS = 8


class LineType(Enum):
    TAG = 1
    COMMENT = 2
    DEFINE = 3
    PROPERTY = 4

class SnapBoltError(Exception):
    pass

class SizeType(Enum):
    FILL = 0
    NO_SIZE = 1

class Line:
    def __init__(self, type : LineType, content : str, indentation : int, pos : list, file, _id : int):

        self.type = type
        self.content = content
        self.indentation = indentation
        
        if self.type == LineType.TAG:
            self.tag = Tag(pos, file, _id, self)
        else:
            self.tag = Property(file, _id, self)

class Property:
    def __init__(self, file, _id, line):
        self.parent = None
        self.file = file
        self.line : Line = line
        self.id = _id

        args = self.line.content.split(": ")
        self.line.content = args[1]
        self.property = args[0]


    def set_value(self):
        self.parent.values[self.property] = self.line.content
        for val in self.parent.values:
            if self.parent.values[val].endswith("\n"): self.parent.values[val] = self.parent.values[val][:-1]
        print(self.parent.values)




class Tag:
    def __init__(self, pos : list, file, _id : int, line : Line):
        self.children = []

        self.values = {}

        self.line = line
        self.file = file
        self.id = _id
        self.size1, self.size2 = 0, 0
        self.parent = None
        args = self.line.content.split(' ')

        self.line.content = ""

        for ele in args:
            if ele == "fill" and self.size1 == 0: 
                self.size1 = SizeType.FILL
            elif ele == "fill" and self.size2 == 0: 
                self.size2 = SizeType.FILL
            elif ele[0] in string.ascii_letters:
                self.line.content += ele
            elif self.size1 == 0:
                self.size1 = int(ele)
            elif self.size2 == 0:
                self.size2 = int(ele)

        p = pos
        
        for ele in p:
            if ele in ("", "\n"): p.remove(ele)

        i = 0
        for ele in p:
            if ele.endswith("\n"): p[i] = ele[:-1]
            i += 1

        self.position = Position(
            (self.convert_to_enum(p[0]) if len(p) >= 1 else (PositionType.NO_POS if self.line.content in ("Main") else PositionType.CENTER)), 
            (p[1] if len(p) >= 2 else 0), 
            (p[2] if len(p) >= 3 else 0), 
            (self.convert_to_enum(p[3]) if len(p) >= 4 else None), 
            (p[4] if len(p) >= 5 else 0), 
            (p[5] if len(p) >= 6 else 0)
        )

        print(self.line.content + ": ", str(self.size1) + " ", str(self.size2))


    def convert_to_enum(self, _str : str):
        if _str == "NO_POS": return PositionType.NO_POS
        if _str == "top": return PositionType.TOP
        if _str == "bottom": return PositionType.BOTTOM
        if _str == "left": return PositionType.LEFT
        if _str == "right": return PositionType.RIGHT
        if _str == "snap_over": return PositionType.SNAP_OVER
        if _str == "snap_under": return PositionType.SNAP_UNDER
        if _str == "center": return PositionType.CENTER

    def get_children(self):
        out : Line = []

        for line in self.file.lines:
            if line.tag is not self and line.tag.id > self.id:
                if line.indentation == self.line.indentation: break
                if line.indentation < self.line.indentation: break
                if line.indentation == self.line.indentation + INDENTATION_INTERVAL: 
                    out.append(line)
                    line.tag.parent = self
                    if line.type == LineType.PROPERTY:
                        line.tag.set_value()

        self.children = out
        #print(self.line.content, [l.content for l in out])

        for line in out:
            if line.type != LineType.PROPERTY: line.tag.get_children()

class Position:
    def __init__(self, pos1 : PositionType, offset1 : int = 0, offset2 : int = 0, pos2 : PositionType = None, offset3 = 0, offset4 = 0):
        self.pos1, self.pos2 = pos1, pos2
        self.offset1, self.offset2 = offset1, offset2
        self.offset3, self.offset4 = offset3, offset4