from Classes import *
from typing import List

class SnapFile:
    def __init__(self, path):
        self.path = path
        self.setup()

    def setup(self):
        self.set_file()
        self.get_lines()

    def set_file(self):
        self.file = open(self.path)

    def get_lines(self):
        self.raw_lines = self.file.read().split('\n')


class SnapData:
    def __init__(self, file : SnapFile):
        self.file = file
        self.tags: List[Tag] = self.gen_tags()

    def gen_tags(self) -> List[Tag]:
        out = []
        for l in self.file.raw_lines:
            lc = self.get_line_content(l)
            out.append(Tag(
                self.get_line_indentation(l), 
                lc[0], 
                Context(
                    Size(lc[1], lc[2]), 
                    Pos(lc[3], lc[4], lc[5], lc[6])
                )
            ))
        return out

    def get_line_content(self, l):
        ls = LineSeparator(l)
        ls.separate()

    def get_line_indentation(self, l) -> int:
        out = 0
        for char in l:
            if char == " ": out += 1
            elif char == "\t": out += 4
            else: break
        return out

class LineSeparator:
    def __init__(self, l):
        self.l = l
        self.i = -1
        self.char = ""
    
    def advance(self):
        self.i += 1
        self.char = self.l[self.i]
    
    def separate(self):
        raw_content = ""
        raw_pos = ""
        is_pos = False
        is_content = False
        self.advance()
        while self.char != "":
            print("debug")
            if self.char == "[":
                self.advance()
                is_content = True
            elif is_content and self.char == "]":
                is_content = False
                is_pos = True
            elif is_content:
                raw_content += self.char
            elif is_pos:
                raw_pos += self.char
            else:
                self.advance()

        pos = raw_pos.split(" ")
        content = raw_content.split(" ")

        print(pos);print(content)
