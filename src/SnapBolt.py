from Compile import Compiler
from Classes import Line, LineType

FILE = open("src/Main.sb")

class File:
    def __init__(self, file):
        self.filedata = file
        self.indentationdata = {}
        self.lines : Line = []

        i = 0
        for line in file.readlines():
            self.indentationdata[i] = self.get_indentation(line); 
            self.lines.append(self.get_line_tag(line, i))
            i += 1

        l : Line = self.lines[0]
        l.tag.get_children()  

    def get_line_tag(self, line, index) -> Line:
        out = ""
        post_line = ""
        trim = 0

        for char in line:
            if char in (" ", "\n"): trim += 1
            else: break

        post_line = line[trim:]

        if post_line.startswith("["):
            trim = 0
            for char in post_line:
                trim += 1
                if char == "]": break
                else: out += char

            pos_text : str = post_line[trim:]
            pos = pos_text.split(" ")
            pos.pop(0)

            return Line(LineType.TAG, out[1:], self.indentationdata[index], pos, self, index)
        elif len(post_line) != 0:
            return Line(LineType.PROPERTY, post_line, self.indentationdata[index], None, self, index)

    def get_indentation(self, line) -> int:
        indentation = 0
        for char in line:
            if char == " ": indentation += 1
            elif char == "\t": indentation += 4
            elif char not in (" ", "\n"): break

        return indentation

    

def main():
    f = File(FILE)
    c = Compiler(f.lines[0], "Test")
    c.compile()

if __name__ == "__main__": 
    main()
