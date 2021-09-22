from typing import List

import GlobalUtils
from SnapCoreDefinitions import Context, Pos, Position, Size, Tag


class SnapFile:
    def __init__(self, path):
        self.path = path
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
        print(self.tags())

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
        c = False
        p = False
        raw_content = ""
        raw_pos = ""
        for char in l:
            if char == "[":
                c = True
            elif char == "]":
                c = False
                p = True
            elif c:
                raw_content += char
            elif p:
                raw_pos += char

        pos = raw_pos.split(" ")
        content = raw_content.split(" ")

        content[:] = [x for x in content if x]
        pos[:] = [x for x in pos if x]

        print(pos, "\n", content)
        print(content[0])

        return [
            content[0],
            int(content[1]) if GlobalUtils.index_in_list(content, 1) else 0,
            int(content[2]) if GlobalUtils.index_in_list(content, 2) else 0,
            Position[pos[0].upper()] if GlobalUtils.index_in_list(pos, 0) else Position.CENTER,
            int(pos[1]) if GlobalUtils.index_in_list(pos, 1) else 0,
            int(pos[2]) if GlobalUtils.index_in_list(pos, 2) else 0,
            Position[pos[3].upper()] if GlobalUtils.index_in_list(pos, 3) else Position.TOP
        ]

    def get_line_indentation(self, l) -> int:
        out = 0
        for char in l:
            if char == " ": out += 1
            elif char == "\t": out += 4
            else: break
        return out
