import string
import random

HtmlTagConverter = {
    "Text": "p",
    "Main": "div"
}

class HtmlTags:
    def __init__(self):
        self.tags = {
            "root": []
        }

class CssTags:
    def __init__(self):
        self.tags = {
            "*": [],
            "body": [],
            "html": []
        }

class Webpage:
    registered_classes = []
    
    def __init__(self):
        self.html = HtmlTags()
        self.css = CssTags()

    @staticmethod    
    def gen_random_class() -> str:
        c = ""
        print(Webpage.registered_classes)
        while True:
            c += random.choice(string.ascii_lowercase)
            print(c)
            if c not in Webpage.registered_classes:
                break
            
        Webpage.registered_classes.append(c)

        return c


class Html:
    def __init__(self, tag, _class, content=None):
        self.tag = tag
        self.content = content
        self.html_class = _class

    def __repr__(self) -> str:
        return (f"<{self.tag} class=\"{self.html_class}\">{self.content}<{self.tag}>" if self.content != None else f"<{self.tag} class=\"{self.html_class}\" />")