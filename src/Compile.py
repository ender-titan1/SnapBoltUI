import os
import os.path
from Classes import *

class Compiler:

    def __init__(self, compiler_data, project_name):
        self.data : Line = compiler_data
        self.project_name = project_name

    def compile(self):
        self.make_output_folder()
        self.generate_webpage()

    def make_output_folder(self):
        if not os.path.exists("../snap bolt output"):
            os.mkdir("../snap bolt output")
        if not os.path.exists(f"../snap bolt output/{self.project_name}"):
            os.mkdir(f"../snap bolt output/{self.project_name}")

    def generate_tags(self, HTML, CSS):
        tags = []
        ele : Line
        for ele in self.data.tag.children:
            print(ele.content)
            if ele.content == "Text":
                p = ""
                offset = "margin-"
                if ele.tag.position.pos1 not in (PositionType.SNAP_UNDER, PositionType.SNAP_OVER, PositionType.TOP, PositionType.BOTTOM):
                    p = "text-align: "
                    p += str(ele.tag.position.pos1).lower().split(".")[1]
                    p += ";"
                if int(ele.tag.position.offset1) < 0:
                    offset += "right: "
                    offset += str(abs(int(ele.tag.position.offset1)))
                    offset += "px;"
                else:
                    offset += "left: "
                    offset += str(abs(int(ele.tag.position.offset1)))
                    offset += "px;"
                
                tags.append("\t\t\t<p style=\"font-size: " + str(ele.tag.size1) + "px;" + p + offset +" \"> " + ele.tag.values["Text"].replace("\"", "") + " </p>\n")
        return tags

    def generate_webpage(self):

        HTML = open("src/templates/htmltemplate.template", "r")
        CSS = open("src/templates/csstemplate.template", "r")

        html = HTML.read().split("$$$")

        tags = self.generate_tags(HTML, CSS)
                

        if not os.path.isfile(f"../snap bolt output/{self.project_name}/Main.html"):
            with open(f'../snap bolt output/{self.project_name}/Main.html', 'w') as f:
                f.write(html[0])
                i = 0
                for tag in tags:
                    f.write(tags[i])
                    i += 1
                f.write(html[1])
        else:
            with open(f'../snap bolt output/{self.project_name}/Main.html', 'w') as f:
                f.write(html[0])
                i = 0
                for tag in tags:
                    f.write(tags[i])
                    i += 1
                f.write(html[1])

        if not os.path.isfile(f"../snap bolt output/{self.project_name}/Main.css"):
            with open(f'../snap bolt output/{self.project_name}/Main.css', 'w') as f:
                f.write(
                    CSS.read()
                    )
        else:
            with open(f'../snap bolt output/{self.project_name}/Main.css', 'w') as f:
                f.write(
                    CSS.read()
                    )



